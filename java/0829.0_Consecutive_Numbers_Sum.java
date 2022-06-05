/*
执行用时：2 ms, 在所有 Java 提交中击败了86.90% 的用户
内存消耗：38.6 MB, 在所有 Java 提交中击败了5.35% 的用户
通过测试用例：170 / 170
*/
class Solution {
    public int consecutiveNumbersSum(int n) {
        int ans = 0;
        for (int i = 1; n > 0; n -= i++) {
            if (0 == n % i) { 
                ans++;
            }
        }
        return ans;
    }
}
