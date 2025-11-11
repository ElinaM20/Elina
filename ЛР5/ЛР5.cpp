#include <iostream>
#include <vector>
using namespace std;
vector<vector<pair<int, int>>> all_paths;
vector<pair<int, int>> path;
vector<vector<bool>> visited;
vector<vector<int>> maze;
void dfs(int r, int c, int rows, int cols) {
    // Проверка границ, стены и посещения
    if (r < 0 || r >= rows || c < 0 || c >= cols || maze[r][c] == 1 || visited[r][c]) {
        return;
    }
    // Добавляем клетку в путь
    path.push_back({r, c});
    visited[r][c] = true;
    // Если дошли до финиша
    if (r == rows - 1 && c == cols - 1) {
        all_paths.push_back(path);
    } else {
        // 4 направления
        dfs(r + 1, c, rows, cols); // вниз
        dfs(r - 1, c, rows, cols); // вверх
        dfs(r, c + 1, rows, cols); // вправо
        dfs(r, c - 1, rows, cols); // влево
    }
    // Возврат (backtrack)
    path.pop_back();
    visited[r][c] = false;
}
int main() {
    int rows = 5, cols = 5;
    maze = {
        {0, 0, 0, 0, 0},
        {1, 1, 0, 1, 0},
        {0, 0, 0, 1, 0},
        {0, 1, 1, 1, 0},
        {0, 0, 0, 0, 0}
    };
    visited.assign(rows, vector<bool>(cols, false));
    dfs(0, 0, rows, cols);

    cout << "Найдено путей: " << all_paths.size() << endl;
    for (int i = 0; i < all_paths.size(); ++i) {
        cout << "Путь " << i + 1 << ": ";
        for (auto p : all_paths[i]) {
            cout << "(" << p.first << "," << p.second << ") ";
        }
        cout << endl;
    }
    return 0;
}


Найдено путей: 2
Путь 1: (0,0) (0,1) (0,2) (1,2) (2,2) (2,1) (2,0) (3,0) (4,0) (4,1) (4,2) (4,3) (4,4) 
Путь 2: (0,0) (0,1) (0,2) (0,3) (0,4) (1,4) (2,4) (3,4) (4,4) 
