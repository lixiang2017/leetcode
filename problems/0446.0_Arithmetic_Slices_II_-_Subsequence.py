'''
DP + hash table
T: O(N^2)
S: O(N^2)

Runtime: 3064 ms, faster than 29.00% of Python3 online submissions for Arithmetic Slices II - Subsequence.
Memory Usage: 52.4 MB, less than 68.64% of Python3 online submissions for Arithmetic Slices II - Subsequence.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [Counter() for _ in range(n)]
        # i -> j
        for j in range(1, n):
            for i in range(j):
                diff = nums[j] - nums[i]
                ans += dp[i][diff]
                dp[j][diff] += dp[i][diff] + 1
        return ans
        
