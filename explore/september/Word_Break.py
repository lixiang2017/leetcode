'''
You are here!
Your runtime beats 37.15 % of python submissions.
'''




class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] and s[j: i + 1] in wordDict:
                    dp[i + 1] = True
        return dp[n]