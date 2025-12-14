import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# Настройки
IMG_SIZE = 250  # размер по меньшей стороне
tf.keras.backend.clear_session()


def load_img(path, max_dim=IMG_SIZE):
    img = tf.io.read_file(path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    shape = tf.cast(tf.shape(img)[:-1], tf.float32)
    long_dim = tf.reduce_max(shape)
    scale = max_dim / long_dim
    new_shape = tf.cast(shape * scale, tf.int32)
    img = tf.image.resize(img, new_shape)
    img = img[tf.newaxis, :]   # (1, h, w, 3)
    return img


def deprocess_img(img):
    img = tf.squeeze(img, axis=0)
    img = tf.clip_by_value(img, 0.0, 1.0)
    return img.numpy()


class NeuralStyleTransfer:
    def __init__(self, content_layers, style_layers):
        self.content_layers = content_layers
        self.style_layers = style_layers

        # VGG19 как feature extractor (предобучена на ImageNet) [web:6][web:20]
        vgg = tf.keras.applications.VGG19(include_top=False,
                                          weights='imagenet')
        vgg.trainable = False

        # порядок: сначала style, потом content
        outputs = [vgg.get_layer(name).output
                   for name in style_layers + content_layers]
        self.model = tf.keras.Model([vgg.input], outputs)

    def _get_feature_representations(self, content_image, style_image):
        """Извлекает списки признаков для стиля и контента."""
        content_input = content_image * 255.0
        style_input = style_image * 255.0

        content_input = tf.keras.applications.vgg19.preprocess_input(content_input)
        style_input = tf.keras.applications.vgg19.preprocess_input(style_input)

        style_outputs = self.model(style_input)
        content_outputs = self.model(content_input)

        num_style = len(self.style_layers)
        num_content = len(self.content_layers)

        style_features = [o for o in style_outputs[:num_style]]
        content_features = [o for o in content_outputs[num_style:num_style + num_content]]

        return style_features, content_features

    def gram_matrix(self, tensor):
        """Gram matrix по каналам: (b, h, w, c) -> (c, c)."""
        x = tf.reshape(tensor, (-1, tf.shape(tensor)[-1]))
        gram = tf.matmul(x, x, transpose_a=True)
        num_locations = tf.cast(tf.shape(x)[0] * tf.shape(x)[1], tf.float32)
        return gram / num_locations

    def content_loss(self, content_features, generated_features):
        """MSE между признаками контента и сгенерированного изображения."""
        loss = 0.0
        for c_feat, g_feat in zip(content_features, generated_features):
            loss += tf.reduce_mean(tf.square(c_feat - g_feat))
        return loss

    def style_loss(self, style_features, generated_features):
        """MSE между Gram-матрицами style и generated.[web:16]"""
        total_loss = 0.0
        for style_feat, gen_feat in zip(style_features, generated_features):
            style_gram = self.gram_matrix(style_feat)
            gen_gram = self.gram_matrix(gen_feat)
            total_loss += tf.reduce_mean(tf.square(style_gram - gen_gram))
        return total_loss

    def total_loss(self, content_features, style_features,
                   gen_content_features, gen_style_features,
                   content_weight=1e4, style_weight=1e-2):
        """Комбинация content и style loss.[web:9][web:16]"""
        c_loss = self.content_loss(content_features, gen_content_features)
        s_loss = self.style_loss(style_features, gen_style_features)
        total = content_weight * c_loss + style_weight * s_loss
        return total, c_loss, s_loss

    @tf.function
    def _train_step(self, generated_image, content_features, style_features,
                    optimizer, content_weight, style_weight):
        with tf.GradientTape() as tape:
            gen_input = generated_image * 255.0
            gen_input = tf.keras.applications.vgg19.preprocess_input(gen_input)
            outputs = self.model(gen_input)

            num_style = len(self.style_layers)
            gen_style_features = [o for o in outputs[:num_style]]
            gen_content_features = [o for o in outputs[num_style:]]

            total_loss, c_loss, s_loss = self.total_loss(
                content_features, style_features,
                gen_content_features, gen_style_features,
                content_weight, style_weight
            )

        grads = tape.gradient(total_loss, generated_image)
        optimizer.apply_gradients([(grads, generated_image)])

        generated_image.assign(tf.clip_by_value(generated_image, 0.0, 1.0))
        return total_loss, c_loss, s_loss

    def transfer_style(self, content_image, style_image, epochs=300,
                       content_weight=1e4, style_weight=1e-2,
                       learning_rate=0.02, show_every=50):
        """
        Основной цикл оптимизации (Adam).
        Плюс расчет pseudo-accuracy = (loss_0 - loss_t) / loss_0.
        """
        style_features, content_features = self._get_feature_representations(
            content_image, style_image
        )

        generated_image = tf.Variable(content_image, dtype=tf.float32)
        optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

        total_losses = []
        content_losses = []
        style_losses = []
        accuracies = []

        initial_loss = None

        for i in range(1, epochs + 1):
            t_loss, c_loss, s_loss = self._train_step(
                generated_image, content_features, style_features,
                optimizer, content_weight, style_weight
            )

            t = float(t_loss.numpy())
            c = float(c_loss.numpy())
            s = float(s_loss.numpy())

            if initial_loss is None:
                initial_loss = t

            acc = (initial_loss - t) / initial_loss if initial_loss > 0 else 0.0

            total_losses.append(t)
            content_losses.append(c)
            style_losses.append(s)
            accuracies.append(acc)

            if i % show_every == 0 or i == 1:
                print(f"Epoch {i}/{epochs} | "
                      f"Total: {t:.2f}, "
                      f"Content: {c:.2f}, "
                      f"Style: {s:.2f}, "
                      f"Accuracy: {acc:.3f}")

        # Визуализация: лоссы + accuracy
        epochs_range = range(1, epochs + 1)
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, total_losses, label='Total loss')
        plt.plot(epochs_range, content_losses, label='Content loss')
        plt.plot(epochs_range, style_losses, label='Style loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.title('Loss')
        plt.legend()
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, accuracies, label='Accuracy', color='green')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.title('Accuracy')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        return generated_image, (total_losses, content_losses, style_losses, accuracies)


# Пути к картинкам в Colab [web:27]
content_path = '/content/content.jpg'
style_path = '/content/style.jpg'

content_img = load_img(content_path)
style_img = load_img(style_path)

# Слои VGG19 [web:6][web:16]
content_layers = ['block5_conv2']
style_layers = [
    'block2_conv1',
    'block3_conv1',
    'block4_conv1',
]

nst = NeuralStyleTransfer(content_layers, style_layers)

# Визуализация исходных картинок
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(deprocess_img(content_img))
plt.title('Content image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(deprocess_img(style_img))
plt.title('Style image')
plt.axis('off')
plt.suptitle('Пары изображений для Neural Style Transfer')
plt.show()

# Запуск переноса стиля
result_img, (tot_l, c_l, s_l, acc) = nst.transfer_style(
    content_img, style_img,
    epochs=500,
    content_weight=1e3,
    style_weight=0.5,
    learning_rate=0.01,
    show_every=50
)

# Показ финального изображения
final_img = deprocess_img(result_img)
plt.figure(figsize=(5, 5))
plt.imshow(final_img)
plt.axis('off')
plt.title('Итоговое стилизованное изображение')
plt.show()