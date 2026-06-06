class Solution {
    public int[] leftRightDifference(int[] nums) {
        int total = 0;
        for (int x: nums) {
            total += x;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            nums[i] = Math.abs(leftSum * 2 + x - total);
            leftSum += x;
        }
        return nums;
    }
}
