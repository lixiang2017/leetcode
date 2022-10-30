/*
Runtime: 142 ms, faster than 95.60% of C# online submissions for Shortest Path in a Grid with Obstacles Elimination.
Memory Usage: 37.7 MB, less than 97.80% of C# online submissions for Shortest Path in a Grid with Obstacles Elimination.
*/
public class Solution {
    static int [][] dirs = {new int[]{-1, 0}, new int[]{1, 0}, new int[]{0, -1}, new int[]{0, 1}};
    
    public int ShortestPath(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;    
        if (k >= m + n - 3) {
            return m + n - 2;
        }
        int[][][] distances = new int[m][][];
        for (int i = 0; i < m; i++) {
            distances[i] = new int[n][];
            for (int j = 0; j < n; j++) {
                distances[i][j] = new int[k + 1];
                Array.Fill(distances[i][j], int.MaxValue);
            }
        }
        distances[0][0][0] = 0;
        Queue<Tuple<int, int, int>> q = new Queue<Tuple<int, int, int>>();
        q.Enqueue(new Tuple<int, int, int>(0, 0, 0));
        while (q.Count > 0) {
            Tuple<int, int, int> state = q.Dequeue();
            int row = state.Item1, col = state.Item2, eliminations = state.Item3;
            int distance = distances[row][col][eliminations];
            if (row == m - 1 && col == n - 1) {
                return distance;
            }
            foreach (int[] dir in dirs) {
                int newRow = row + dir[0], newCol = col + dir[1];
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) {
                    if (grid[newRow][newCol] == 0) {
                        if (distances[newRow][newCol][eliminations] == int.MaxValue) {
                            distances[newRow][newCol][eliminations] = distance + 1;
                            q.Enqueue(new Tuple<int, int, int>(newRow, newCol, eliminations));
                        }
                    } else {
                        if (eliminations < k && distances[newRow][newCol][eliminations + 1] == int.MaxValue) {
                            distances[newRow][newCol][eliminations + 1] = distance + 1;
                            q.Enqueue(new Tuple<int, int, int>(newRow, newCol, eliminations + 1));
                        }
                    }
                }
            }
        }
        return -1;
    }
}
