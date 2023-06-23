'''
Runtime: 2846 ms, faster than 78.72% of Python3 online submissions for Longest Arithmetic Subsequence.
Memory Usage: 24.2 MB, less than 91.53% of Python3 online submissions for Longest Arithmetic Subsequence.
'''
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # [-500, 500] -> [0, 1000]
        delta = 500
        n = len(nums)
        dp = [[1] * 1001 for _ in range(n)]
        # i -> j
        for j in range(1, n):
            for i in range(j):
                diff = nums[j] - nums[i] + delta
                dp[j][diff] = max(dp[j][diff], dp[i][diff] + 1)
                
        return max(max(row) for row in dp)
        
        