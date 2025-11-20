def greedy_coloring(adj_list):
    n = len(adj_list)
    colors = [-1] * n  # -1 означает, что цвет не назначен
    
    for v in range(n):
        # Собираем используемые цвета соседей
        used = set()
        for neighbor in adj_list[v]:
            if colors[neighbor] != -1:
                used.add(colors[neighbor])
        
        # Назначаем минимальный доступный цвет
        color = 0
        while color in used:
            color += 1
        colors[v] = color
    
    return colors

# Ввод данных с клавиатуры
print("Введите количество вершин графа:")
n = int(input())

print("Введите списки смежности для каждой вершины (через пробелы, 0-индексация):")
adj_list = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_list.append(row)

# Выполняем раскраску
result = greedy_coloring(adj_list)

# Выводим результат
print("Результаты раскраски (номер вершины: цвет):")
for i, color in enumerate(result):
    print(f"{i}: {color}")

print(f"Использовано цветов: {max(result) + 1}")






Введите количество вершин графа:
5
Введите списки смежности для каждой вершины (через пробелы, 0-индексация):
1 2
0 3
4 1
2 3
2 0
Результаты раскраски (номер вершины: цвет):
0: 0
1: 1
2: 0
3: 1
4: 1
Использовано цветов: 2

