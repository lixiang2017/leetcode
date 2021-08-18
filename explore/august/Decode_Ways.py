'''
DP
Time: O(N)
Space: O(N)

You are here!
Your memory usage beats 40.75 % of python3 submissions.
You are here!
Your runtime beats 67.90 % of python3 submissions.

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if not s or ('0' == s[0]):
            return 0
        if 1 == N:
            return 1
        
        codes = set(map(str, range(1, 27)))
        dp = [0] * (N)
        # init, for dp[0]
        if s[0] != '0':
            dp[0] = 1
        # for dp[1]
        if s[0] in codes and s[1] in codes:
            dp[1] += 1
        if s[:2] in codes:
            dp[1] += 1
        # run
        for i in range(2, N):
            if s[i] in codes:
                dp[i] += dp[i - 1]
            if s[i - 1: i + 1] in codes:
                dp[i] += dp[i - 2]
        
        return dp[-1]
