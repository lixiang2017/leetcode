'''
You are here!
Your runtime beats 16.62 % of python submissions.
'''


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        sum_all = sum(nums)
        if sum_all % 2  != 0:  return False
        half = sum_all / 2

        # dp[size][half]  # set dp[..][0] to True, set dp[0][..] to False 
        dp = [[True] + [False for i in range(half)] for j in range(size + 1)]
        
        for i in range(1, size + 1):
            for j in range(half + 1):
                if j - nums[i - 1] >= 0: 
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # print 'dp: ', dp
        return dp[size][half]

        
