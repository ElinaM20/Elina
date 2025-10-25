АЛГОРИТМЫ СОРТИРОВКИ

СОРТИРОВКА ВЫБОРОМ (SELECTION SORT)

#include <iostream> // Подключаем библиотеку ввода-вывода
// Функция для сортировки массива методом выбора
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; ++i) {   // Внешний цикл проходит по элементам массива слева направо
        int minIndex = i;               // Предполагаем, что минимальный элемент находится на текущей позиции
        
        // Внутренний цикл ищет наименьший элемент среди оставшихся элементов справа
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) { // Если нашли меньший элемент, обновляем индекс минимального элемента
                minIndex = j;
            }
        }
        // Меняем местами найденный минимальный элемент с элементом на текущей позиции
        std::swap(arr[i], arr[minIndex]); // Используем стандартную функцию swap для перестановки значений
    }
}
// Вспомогательная функция для вывода отсортированного массива
void printArray(const int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << ' ';      // Печать каждого элемента массива
    }
    std::cout << '\n';                   // Перевод строки после печати всех элементов
}
// Главная функция программы
int main() {
    const int SIZE = 8;                 // Определяем размер массива вручную
    int array[] = {64, 25, 12, 22, 11}; // Исходный массив для сортировки
    std::cout << "Исходный массив:\n";
    printArray(array, SIZE);            // Показываем исходный несортированный массив
    selectionSort(array, SIZE);         // Сортируем массив функцией сортировки выбором
    std::cout << "\nОтсортированный массив:\n";
    printArray(array, SIZE);            // Показываем отсортированный массив
    return 0;                           // Завершаем программу успешно
}

Исходный массив:
64 25 12 22 11 0 -361142528 1417856667 
Отсортированный массив:
-361142528 0 11 12 22 25 64 1417856667 

СОРТИРОВКА СЛИЯНИЕМ (MERGE SORT)

#include <iostream>
#include <vector>
using namespace std;
// Вспомогательная функция для объединения двух отсортированных частей массива
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;           // Длина левой части
    int n2 = right - mid;              // Длина правой части
    vector<int> L(n1), R(n2);          // Создание временных массивов для хранения обеих половинок
    // Копируем данные в временные массивы
    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];           // Левая половина
    }
    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];       // Правая половина
    } 
    // Индексы для трех массивов
    int i = 0, j = 0, k = left;
    // Объединяем обе половинки в основной массив
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {             // Если левый элемент меньше или равен правому
            arr[k++] = L[i++];          // Добавляем элемент из левой половинки
        } else {
            arr[k++] = R[j++];          // Иначе добавляем элемент из правой половинки
        }
    }
    // Остаточные элементы из левой половинки (если остались)
    while (i < n1) {
        arr[k++] = L[i++];
    }
    // Остаточные элементы из правой половинки (если остались)
    while (j < n2) {
        arr[k++] = R[j++];
    }
}
// Рекурсивная функция сортировки слиянием
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {                            // Пока левая граница меньше правой
        int mid = left + (right - left) / 2;       // Находим середину массива
        // Рекурсивно сортируем левую половину
        mergeSort(arr, left, mid);
        // Рекурсивно сортируем правую половину
        mergeSort(arr, mid + 1, right);
        // Соединяем отсортированные половинки
        merge(arr, left, mid, right);
    }
}
// Основная функция для запуска сортировки
void performMergeSort(vector<int>& arr) {
    mergeSort(arr, 0, arr.size() - 1);  // Запускаем рекурсию с границами 0 и length - 1
}
// Функция для вывода массива
void printArray(const vector<int>& arr) {
    for (auto num : arr) {
        cout << num << " ";
    }
    cout << endl;
}
// Точка входа в программу
int main() {
    vector<int> input = {38, 27, 43, 3, 9, 82, 10};
    cout << "Исходный массив: ";
    printArray(input);
    performMergeSort(input);  // Запускаем сортировку
    cout << "Отсортированный массив: ";
    printArray(input);
    return 0;
}

Исходный массив: 38 27 43 3 9 82 10 
Отсортированный массив: 3 9 10 27 38 43 82

ПИРАМИДАЛЬНАЯ СОРТИРОВКА (HEAP SORT) 

#include <iostream>
#include <vector>
using namespace std;
// Функция heapify восстанавливает свойство кучи
void heapify(vector<int>& arr, int n, int root) {
    int largest = root;     // Начать с корня
    int left_child = 2 * root + 1;  // Левый потомок
    int right_child = 2 * root + 2; // Правый потомок
    // Если левый потомок существует и больше родителя
    if (left_child < n && arr[left_child] > arr[largest]) {
        largest = left_child;
    }
    // Если правый потомок существует и больше текущего максимального узла
    if (right_child < n && arr[right_child] > arr[largest]) {
        largest = right_child;
    }
    // Если корень изменился, поменять местами и вызвать heapify рекурсивно
    if (largest != root) {
        swap(arr[root], arr[largest]);
        heapify(arr, n, largest); // Рекурсивно восстанавливаем кучу
    }
}
// Основная функция сортировки Heap Sort
void heapSort(vector<int>& arr) {
    int n = arr.size();
    // Строим max-кучу (преобразование массива в двоичную кучу)
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i); // Восстанавливаем свойства кучи для каждого элемента
    }
    // Один за другим извлекаем максимальные элементы из кучи
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]); // Максимальный элемент переносим в конец
        heapify(arr, i, 0);   // Восстанавливаем кучу для оставшейся части
    }
}
// Функция для вывода массива
void printArray(const vector<int>& arr) {
    for (int val : arr) {
        cout << val << " ";
    }
    cout << endl;
}
// Главный блок программы
int main() {
    vector<int> arr = {12, 11, 13, 5, 6, 7};
    cout << "Исходный массив: ";
    printArray(arr);
    heapSort(arr); // Производим сортировку
    cout << "Отсортированный массив: ";
    printArray(arr);
    return 0;
}

Исходный массив: 12 11 13 5 6 7 
Отсортированный массив: 5 6 7 11 12 13

АЛГОРИТМЫ ПОИСКА

БИНАРНЫЙ (ДВОИЧНЫЙ, ДИХОТОМИЧЕСКИЙ) ПОИСК

#include <iostream>
#include <vector>
using namespace std;
// Функция для бинарного поиска
int binarySearch(const vector<int>& arr, int target) {
    int low = 0;                   // Нижняя граница поиска
    int high = arr.size() - 1;     // Верхняя граница поиска
    while (low <= high) {          // Пока нижняя граница не пересекла верхнюю границу
        int mid = low + (high - low) / 2;  // Рассчитываем центральный индекс
        if (arr[mid] == target) {  // Если элемент найден, возвращаем его индекс
            return mid;
        } else if (arr[mid] < target) {  // Если целевой элемент больше центрального
            low = mid + 1;              // Сужаем область поиска вправо
        } else {                        // Если целевой элемент меньше центрального
            high = mid - 1;            // Сужаем область поиска влево
        }
    }
    return -1;                         // Если элемент не найден, возвращаем -1
}
// Функция для демонстрации работы алгоритма
int main() {
    vector<int> arr = {2, 3, 4, 10, 40};  // Упорядоченный массив
    int target = 10;                      // Целевой элемент для поиска
    int result = binarySearch(arr, target);  // Вызываем функцию поиска
    if(result != -1) {
        cout << "Элемент найден на позиции: " << result << endl;
    } else {
        cout << "Элемент не найден." << endl;
    }
    return 0;
}

Элемент найден на позиции: 3

ИНТЕРПОЛИРУЮЩИЙ ПОИСК

#include <iostream>
#include <vector>
using namespace std;
// Функция для интерполирующего поиска
int interpolationSearch(const vector<int>& arr, int target) {
    int low = 0;                             // Нижний индекс поиска
    int high = arr.size() - 1;               // Верхний индекс поиска
    while ((low <= high) && (target >= arr[low]) && (target <= arr[high])) {
        // Расчет приблизительной позиции искомого элемента
        int pos = low + (((double)(high - low) /
                          (arr[high] - arr[low])) *
                         (target - arr[low]));
        // Если найден элемент, возвращаем его индекс
        if (arr[pos] == target) {
            return pos;
        }
        // Если цель меньше элемента в позиционной точке, идем влево
        if (arr[pos] < target) {
            low = pos + 1;
        }
        // Если цель больше элемента в позиционной точке, идем вправо
        else {
            high = pos - 1;
        }
    }
    return -1;                               // Если элемент не найден
}
// Пример использования
int main() {
    vector<int> arr = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
    int target = 18;
    int result = interpolationSearch(arr, target);
    if (result != -1) {
        cout << "Элемент найден на позиции: " << result << endl;
    } else {
        cout << "Элемент не найден." << endl;
    }
    return 0;
}

Элемент найден на позиции: 4
