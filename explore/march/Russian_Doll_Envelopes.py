'''
approach: Sort + DP
Time: O(NlogN + N^2)
Space: O(N)

You are here!
Your runtime beats 11.48 % of python submissions.
You are here!
Your memory usage beats 22.49 % of python submissions.
'''


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        N = len(envelopes)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
