
/*
approach: Brute Force
Time: O(MN)
Space: O(1)

执行用时：20 ms, 在所有 Java 提交中击败了6.80%的用户
内存消耗：44.2 MB, 在所有 Java 提交中击败了22.11%的用户
*/


class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
}

