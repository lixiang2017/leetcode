'''
approach: Dynamic Programming with State Compression
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 89.55 % of python submissions.
You are here!
Your memory usage beats 79.37 % of python submissions.
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
        # dp = [0 for _ in range(size + 1)]
        # dp[0] = 1
        before = after = 1
        for i in range(1, size):
            if '0' == s[i]:
                # dp[i] = 0
                after = 0
            else:
                pass
                # dp[i] = dp[i - 1]
                # after = before

            if (s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) <= 6)):
                after += before
                before = after - before
            else:
                before = after

        return after

