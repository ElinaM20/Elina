import java.util.*;
public class MazePaths {
    private static List<List<int[]>> allPaths = new ArrayList<>();
    private static List<int[]> path = new ArrayList<>();
    private static boolean[][] visited;
    private static int[][] maze;

    public static void dfs(int r, int c, int rows, int cols) {
        // Проверка границ, стены и посещения
        if (r < 0 || r >= rows || c < 0 || c >= cols || maze[r][c] == 1 || visited[r][c]) {
            return;
        }
        // Добавляем клетку в путь
        path.add(new int[]{r, c});
        visited[r][c] = true;
        // Если финиш достигнут
        if (r == rows - 1 && c == cols - 1) {
            allPaths.add(new ArrayList<>(path));
        } else {
            // 4 направления
            dfs(r + 1, c, rows, cols); // вниз
            dfs(r - 1, c, rows, cols); // вверх
            dfs(r, c + 1, rows, cols); // вправо
            dfs(r, c - 1, rows, cols); // влево
        }
        // Возврат (backtrack)
        path.remove(path.size() - 1);
        visited[r][c] = false;
    }
    public static void main(String[] args) {
        int rows = 5, cols = 5;
        maze = new int[][]{
            {0, 0, 0, 0, 0},
            {1, 1, 0, 1, 0},
            {0, 0, 0, 1, 0},
            {0, 1, 1, 1, 0},
            {0, 0, 0, 0, 0}
        };
        visited = new boolean[rows][cols];
        dfs(0, 0, rows, cols);
        System.out.println("Найдено путей: " + allPaths.size());
        for (int i = 0; i < allPaths.size(); i++) {
            System.out.print("Путь " + (i + 1) + ": ");
            for (int[] p : allPaths.get(i)) {
                System.out.print("(" + p[0] + "," + p[1] + ") ");
            }
            System.out.println();
        }
    }
}


Найдено путей: 2
Путь 1: (0,0) (0,1) (0,2) (1,2) (2,2) (2,1) (2,0) (3,0) (4,0) (4,1) (4,2) (4,3) (4,4) 
Путь 2: (0,0) (0,1) (0,2) (0,3) (0,4) (1,4) (2,4) (3,4) (4,4) 
