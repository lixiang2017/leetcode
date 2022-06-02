/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Running Sum of 1d Array.
Memory Usage: 43.3 MB, less than 42.33% of Java online submissions for Running Sum of 1d Array.
*/

class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        ans[0] = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            ans[i] = ans[i - 1] + nums[i];
        }
        return ans;
    }
}


/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Running Sum of 1d Array.
Memory Usage: 42.9 MB, less than 67.01% of Java online submissions for Running Sum of 1d Array.
*/
class Solution {
    public int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
}

