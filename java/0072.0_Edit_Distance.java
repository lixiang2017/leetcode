/*
执行用时：5 ms, 在所有 Java 提交中击败了55.32% 的用户
内存消耗：41.4 MB, 在所有 Java 提交中击败了38.00% 的用户
通过测试用例：1146 / 1146
*/
class Solution {
    public int minDistance(String word1, String word2) {
        int n1 = word1.length(), n2 = word2.length();
        int[][] dp = new int[n1 + 1][n2 + 1];
        // the first row
        for (int j = 1; j <= n2; j++) {
            dp[0][j] = j;
        }
        // the first column
        for (int i = 1; i <= n1; i++) {
            dp[i][0] = i;
        }
        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(Math.min(dp[i - 1][j - 1], dp[i][j - 1]), dp[i - 1][j]);
                }
            }
        }
        return dp[n1][n2];
    }
}
