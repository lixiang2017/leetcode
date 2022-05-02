/*
执行用时：3 ms, 在所有 Java 提交中击败了73.51% 的用户
内存消耗：42 MB, 在所有 Java 提交中击败了28.92% 的用户
通过测试用例：68 / 68
*/
class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int maxx = nums[0], minx = nums[0];
        for (int x: nums) {
            maxx = Math.max(x, maxx);
            minx = Math.min(x, minx);
        }
        return Math.max(0, maxx - minx - 2 * k);
    }
}
