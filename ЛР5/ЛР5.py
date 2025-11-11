def find_all_paths(maze):
    rows, cols = len(maze), len(maze[0])
    paths = []
    visited = [[False] * cols for _ in range(rows)]
    def dfs(r, c, path):
        # Если вышли за границы или клетка заблокирована или уже пройдена
        if r < 0 or r >= rows or c < 0 or c >= cols or maze[r][c] == 1 or visited[r][c]:
            return
        # Добавляем текущую клетку в путь
        path.append((r, c))
        visited[r][c] = True
        # Если достигли финиша — сохраняем путь
        if r == rows - 1 and c == cols - 1:
            paths.append(path[:])  # копируем путь
        else:
            # Исследуем все 4 направления
            dfs(r + 1, c, path)  # вниз
            dfs(r - 1, c, path)  # вверх
            dfs(r, c + 1, path)  # вправо
            dfs(r, c - 1, path)  # влево
        # Возвращаемся (backtrack)
        path.pop()
        visited[r][c] = False
    dfs(0, 0, [])
    return paths
# Пример лабиринта (0 — проход, 1 — стена)
maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
all_paths = find_all_paths(maze)
print(f"Найдено путей: {len(all_paths)}")
for i, path in enumerate(all_paths, 1):
    print(f"Путь {i}: {path}")


Найдено путей: 2
Путь 1: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
Путь 2: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
