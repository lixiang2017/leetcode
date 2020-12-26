'''
You are here!
Your runtime beats 89.55 % of python submissions.

approach: Dynamic Programming
Time: O(N)
Space: O(N)

https://www.cnblogs.com/grandyang/p/4313384.html
'''



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or '0' == s[0]:
            return 0
        
        size = len(s)
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        for i in range(1, size + 1):
            if '0' == s[i - 1]:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
            
            if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and int(s[i - 1]) <= 6)):
                dp[i] += dp[i - 2]
        return dp[-1]
