'''
You are here!
Your runtime beats 43.89 % of python submissions.
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
        
        for interval_len in range(1, size + 1):
            for i in range(1, size - interval_len + 2):
                j = i + interval_len - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j])
        
        # print 
        #for i in range(size + 2):
        #    print dp[i]
        
        return dp[1][size]

'''
Your input
[3,1,5,8]
Your stdout
[0, 0, 0, 0, 0, 0]
[0, 3, 30, 159, 167, 0]
[0, 0, 15, 135, 159, 0]
[0, 0, 0, 40, 48, 0]
[0, 0, 0, 0, 40, 0]
[0, 0, 0, 0, 0, 0]

Your answer
167
Expected answer
167

'''

