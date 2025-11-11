Алгоритмы сортировки

Блочная (корзинная) сортировка

def bucket_sort(arr):
    """
    Реализует алгоритм блочной сортировки.
    Параметры:
    arr - список чисел, который нужно отсортировать.
    Возвращает отсортированный список.
    """
    # Если массив пуст или содержит один элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr
    
    # Находим максимальное и минимальное значения в массиве
    min_val = min(arr)
    max_val = max(arr)
    
    # Определяем количество блоков (бакетов) и их размер
    bucket_count = len(arr)  # Кол-во блоков равно кол-ву элементов
    bucket_size = (max_val - min_val) / bucket_count  # Ширина каждого блока
    
    # Создаём пустые блоки (списки)
    buckets = [[] for _ in range(bucket_count)]
    
    # Распределяем элементы по блокам
    for num in arr:
        # Вычисляем номер блока, в который попадёт текущий элемент
        idx = int((num - min_val) / bucket_size)
        # Предохраняемся от вылета за границы последнего блока
        if idx == bucket_count:
            idx -= 1
        buckets[idx].append(num)
    
    # Сортируем каждый блок индивидуально
    for i in range(bucket_count):
        # Применяем встроенную сортировку Python (можно использовать любую другую)
        buckets[i].sort()
    
    # Собираем отсортированные блоки в один массив
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Демонстрация работы
if __name__ == "__main__":
    example_list = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Исходный массив:", example_list)
    sorted_list = bucket_sort(example_list)
    print("Отсортированный массив:", sorted_list)

Исходный массив: [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
Отсортированный массив: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]

Блинная сортировка

def flip(arr, k):
    """
    Переворачивает (reverse) первые k элементов массива.
    :param arr: Исходный массив
    :param k: Сколько элементов перевернуть (счет с 1)
    """
    start = 0
    end = k - 1  # Индексация с 0, поэтому минус 1
    while start < end:
        # Меняем местами первый и последний элементы, постепенно двигаясь внутрь
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def find_max(arr, n):
    """
    Находит индекс максимального элемента в части массива от 0 до n-1.
    :param arr: Исходный массив
    :param n: Индекс, до которого нужно искать
    :return: Индекс максимального элемента
    """
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def pancake_sort(arr):
    """
    Реализует алгоритм блинной сортировки.
    :param arr: Исходный массив
    :return: Отсортированный массив
    """
    curr_size = len(arr)
    while curr_size > 1:
        # Находим индекс максимального элемента в текущей части массива
        max_idx = find_max(arr, curr_size)
        
        # Если максимальный элемент уже на последнем месте, перейти к следующему шагу
        if max_idx != curr_size - 1:
            # Переворачиваем массив, чтобы максимальный элемент попал на верх
            flip(arr, max_idx + 1)
            
            # Переворачиваем массив, чтобы максимальный элемент встал на своё место
            flip(arr, curr_size)
        
        # Уменьшаем рабочую область массива
        curr_size -= 1
    return arr

# Демонстрация работы
if __name__ == "__main__":
    example_list = [3, 6, 2, 7, 1]
    print("Исходный массив:", example_list)
    sorted_list = pancake_sort(example_list)
    print("Отсортированный массив:", sorted_list)

Исходный массив: [3, 6, 2, 7, 1]
Отсортированный массив: [1, 2, 3, 6, 7]

Сортировка бусинами (гравитационная)

def bead_sort(arr):
    """
    Реализует алгоритм сортировки бусинами (bead sort).
    Параметры:
    arr - список положительных целых чисел, который нужно отсортировать.
    Возвращает отсортированный список.
    """
    # Находим максимальный элемент массива, чтобы задать высоту матриц
    max_num = max(arr)
    
    # Создаем матрицу бусин (единиц) размером M x N, где M - количество элементов, N - максимальный элемент
    beads_matrix = [[1 if num > row else 0 for col in range(max_num)] for row, num in enumerate(arr)]
    
    # Поворачиваем матрицу на 90 градусов против часовой стрелки и сбрасываем бусы вниз
    transposed_beads = zip(*beads_matrix)  # транспонирование матрицы
    dropped_beads = [sorted(col, reverse=True) for col in transposed_beads]  # сброс бусин вниз
    
    # Поворачиваем матрицу обратно и считаем количество ненулевых элементов в каждой строке
    result = [sum(row) for row in zip(*dropped_beads)]
    
    return result

# Демонстрация работы
if __name__ == "__main__":
    example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Исходный массив:", example_list)
    sorted_list = bead_sort(example_list)
    print("Отсортированный массив:", sorted_list)

Исходный массив: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Отсортированный массив: [9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0]

Алгоритмы поиска

Поиск скачками (Jump Search)

def jump_search_fixed_block(arr, target):
    """
    Реализует алгоритм поиска скачками с фиксированной длиной блока m = n.
    Параметры:
    arr - отсортированный массив, в котором ведется поиск.
    target - искомое значение.
    Возвращает индекс найденного элемента или -1, если элемент не найден.
    """
    n = len(arr)  # Длина массива
    block_length = n  # Длина блока равна длине массива
    
    # Шаг 1: Делим массив на блоки длины m = n и прыгаем вперёд
    prev = 0  # Индекс предыдущей позиции
    next_pos = block_length  # Следующая позиция
    
    # Шаг 2: Алгоритм прыгает вперёд на m элементов, пока не найдёт элемент, больше или равный искомому
    while next_pos < n and arr[next_pos] < target:
        prev = next_pos
        next_pos += block_length
    
    # Шаг 3: Если найденный элемент больше искомого, выполняется линейный поиск в предыдущем блоке
    for i in range(prev, min(next_pos, n)):
        if arr[i] == target:
            return i
    
    return -1  # Если элемент не найден

# Демонстрация работы
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11
    result = jump_search_fixed_block(arr, target)
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}.")
    else:
        print(f"Элемент {target} не найден.")

Элемент 11 найден на позиции 5.

Экспоненциальный поиск (Exponential Search)

def exponential_search(arr, target):
    """
    Реализует алгоритм экспоненциального поиска.
    Параметры:
    arr - отсортированный массив, в котором ведется поиск.
    target - искомое значение.
    Возвращает индекс найденного элемента или -1, если элемент не найден.
    """
    if arr[0] == target:  # Если первый элемент совпадает с искомым, вернуть его индекс
        return 0
    
    # Находим индекс, начиная с двойного увеличения
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2  # Удвоение индекса
    
    # Диапазон для бинарного поиска
    low = i // 2  # Нижняя граница
    high = min(i, len(arr) - 1)  # Верхняя граница
    
    # Используем встроенную функцию bisect_left для бинарного поиска
    from bisect import bisect_left
    position = bisect_left(arr, target, low, high + 1)
    
    # Проверяем, нашел ли бисект нужный элемент
    if position != len(arr) and arr[position] == target:
        return position
    else:
        return -1

# Демонстрация работы
if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    target = 55
    result = exponential_search(arr, target)
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}.")
    else:
        print(f"Элемент {target} не найден.")

Элемент 55 найден на позиции 10.

Тернарный поиск (Ternary Search)

def recursive_ternary_search(arr, target, left, right):
    """
    Реализует рекурсивный тернарный поиск в отсортированном массиве.
    Параметры:
    arr - отсортированный массив, в котором ведется поиск.
    target - искомое значение.
    left - левая граница поиска.
    right - правая граница поиска.
    Возвращает индекс найденного элемента или -1, если элемент не найден.
    """
    if left > right:
        return -1  # Если область поиска пуста, элемент не найден
    
    # Вычисляем две трети массива
    third1 = left + (right - left) // 3
    third2 = right - (right - left) // 3
    
    # Если искомый элемент найден в одной из точек
    if arr[third1] == target:
        return third1
    elif arr[third2] == target:
        return third2
    
    # Сужаем область поиска
    if target < arr[third1]:
        return recursive_ternary_search(arr, target, left, third1 - 1)
    elif target > arr[third2]:
        return recursive_ternary_search(arr, target, third2 + 1, right)
    else:
        return recursive_ternary_search(arr, target, third1 + 1, third2 - 1)

# Демонстрация работы
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = recursive_ternary_search(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"Элемент {target} найден на позиции {result}.")
    else:
        print(f"Элемент {target} не найден.")

Элемент 7 найден на позиции 6.

