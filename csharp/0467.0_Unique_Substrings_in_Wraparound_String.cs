/*
执行用时：56 ms, 在所有 C# 提交中击败了100.00% 的用户
内存消耗：36.9 MB, 在所有 C# 提交中击败了57.14% 的用户
通过测试用例：81 / 81
*/

public class Solution {
    public int FindSubstringInWraproundString(string p) {
        int[] dp = new int[26];
        int k = 0;
        for (int i = 0; i < p.Length; ++i) {
            if (i > 0 && (p[i] - p[i - 1] + 26) % 26 == 1) {
                ++k;
            } else {
                k = 1;
            }
            dp[p[i] - 'a'] = Math.Max(dp[p[i] - 'a'], k);
        }
        return dp.Sum();
    }
}
