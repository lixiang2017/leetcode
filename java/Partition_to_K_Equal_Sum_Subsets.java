/*
DP

You are here!
Your runtime beats 23.40 % of java submissions.
You are here!
Your memory usage beats 20.43 % of java submissions.
*/

class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        if (1 == k) {
            return true;
        }
        int len = nums.length;
        Arrays.sort(nums);
        int sum = 0;
        for (int num: nums) {
            sum += num;
        }
        if (sum % k != 0) {
            return false;
        }
        int target = sum / k;
        if (nums[len - 1] > target) {
            return false;
        }
        int size = 1 << len;
        boolean[] dp = new boolean[size];
        dp[0] = true;
        int[] currentSum = new int[size];
        for (int i = 0; i < size; ++i) {
            if (!dp[i]) {
                continue;
            }
            for (int j = 0; j < len; ++j) {
                if ((i & (1 << j)) != 0) {
                    continue;
                }
                int next = i | (1 << j);
                if (dp[next]) {
                    continue;
                }
                if ((currentSum[i] % target) + nums[j] <= target) {
                    currentSum[next] = currentSum[i] + nums[j];
                    dp[next] = true;
                } else {
                    break;
                }
            }
        }
        return dp[size - 1];
    }
}
