/*
Runtime: 144 ms, faster than 74.77% of C# online submissions for Toeplitz Matrix.
Memory Usage: 41.7 MB, less than 23.36% of C# online submissions for Toeplitz Matrix.
*/

public class Solution {
    public bool IsToeplitzMatrix(int[][] matrix) {
        int rowLen = matrix.Length;
        int colLen = matrix[0].Length;
        for (int i = 0; i < rowLen - 1; i++) {
            for (int j = 0; j < colLen - 1; j++) {
                if (matrix[i][j] != matrix[i + 1][j + 1]) return false;
            }
        }
        return true;
    }
}
