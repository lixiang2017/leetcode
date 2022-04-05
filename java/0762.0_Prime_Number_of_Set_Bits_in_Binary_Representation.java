/*
执行用时：2 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：38.2 MB, 在所有 Java 提交中击败了62.61% 的用户
通过测试用例：202 / 202
*/
class Solution {
    public int countPrimeSetBits(int left, int right) {
        int ans = 0;
        for (int x = left; x <= right; x++) {
            ans += 665772 >> Integer.bitCount(x) & 1;
        }
        return ans;
    }
}
