/*
执行用时：1 ms, 在所有 Java 提交中击败了91.88% 的用户
内存消耗：38.9 MB, 在所有 Java 提交中击败了81.15% 的用户
*/
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n << 1];
        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        return ans;
    }
}
