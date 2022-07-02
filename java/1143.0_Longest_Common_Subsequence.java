/*
DP, T: O(MN), S: O(MN)

执行用时：14 ms, 在所有 Java 提交中击败了13.50% 的用户
内存消耗：45.2 MB, 在所有 Java 提交中击败了42.38% 的用户
通过测试用例：45 / 45
*/

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] f = new int[m + 1][n + 1];
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    f[i][j] = f[i - 1][j - 1] + 1;
                }
                f[i][j] = Math.max(f[i - 1][j], f[i][j]);
                f[i][j] = Math.max(f[i][j - 1], f[i][j]);
            }
        }
        return f[m][n];
    }
}
