'''
approach: DP
Time: O(target * N)
Space: O(target)

Runtime: 53 ms, faster than 72.51% of Python3 online submissions for Combination Sum IV.
Memory Usage: 13.8 MB, less than 80.97% of Python3 online submissions for Combination Sum IV.
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]
