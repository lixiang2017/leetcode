/*
执行用时：11 ms, 在所有 Java 提交中击败了15.87% 的用户
内存消耗：41 MB, 在所有 Java 提交中击败了76.19% 的用户
通过测试用例：81 / 81
*/
class Solution {
    public int findSubstringInWraproundString(String p) {
        int[] dp = new int[26];
        int k = 0;
        for (int i= 0; i < p.length(); ++i) {
            if (i > 0 && (p.charAt(i) - p.charAt(i - 1) + 26) % 26 == 1) {
                ++k;
            } else {
                k = 1;
            }
            dp[p.charAt(i) - 'a'] = Math.max(dp[p.charAt(i) - 'a'], k);
        }
        return Arrays.stream(dp).sum();
    }
}
