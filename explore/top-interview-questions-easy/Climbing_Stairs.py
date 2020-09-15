'''
You are here!
Your runtime beats 10.09 % of python submissions
'''



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 50
        if 1 == n:
            return 1
        elif 2 == n:
            return 2

        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
