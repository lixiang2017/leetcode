/*
执行用时：5 ms, 在所有 Java 提交中击败了18.69% 的用户
内存消耗：38.6 MB, 在所有 Java 提交中击败了89.62% 的用户
通过测试用例：122 / 122
*/
class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != i) return i;
        }
        return nums[nums.length - 1] + 1;
    }
}
