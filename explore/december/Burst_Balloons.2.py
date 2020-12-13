'''
Approach: DFS/Recursive

You are here!
Your runtime beats 18.33 % of python submissions.
'''

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(size + 2)] for _ in range(size + 2)]
        return self.burst(nums, dp, 1, size)
    
    def burst(self, nums, dp, i, j):
        if i > j: return 0
        if dp[i][j] > 0: return dp[i][j]
        res = 0
        for k in range(i, j + 1):
            res = max(res, nums[i - 1] * nums[k] * nums[j + 1] + 
                      self.burst(nums, dp, i, k - 1) + 
                      self.burst(nums, dp, k + 1, j))
        
        dp[i][j] = res
        return res
