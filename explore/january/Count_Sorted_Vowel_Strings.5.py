'''
approach: DP
Time: O(5 * N) = O(N)
Space: O(N)

You are here!
Your runtime beats 28.42 % of python submissions.
You are here!
Your memory usage beats 90.07 % of python submissions.
'''


class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a e i o u
        # dp[i][j] means count for a i+1 - length string ending with j-th char
        dp = [[1 for _ in range(5)] for __ in range(n + 1)]
        
        for i in range(1, n + 1):
            # ends with 'a'
            dp[i][0] = dp[i - 1][0]
            # ends with 'e'
            dp[i][1] = dp[i - 1][0] + dp[i - 1][1]
            # ends with 'i'
            dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
            # ends with 'o'
            dp[i][3] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            # ends with 'u'
            dp[i][4] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]
        
        return dp[n][4]



'''
approach: DP with State Compression
Time: O(N)
Space: O(1)


You are here!
Your runtime beats 60.96 % of python submissions.
You are here!
Your memory usage beats 45.89 % of python submissions.
'''



class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a e i o u
        # # dp[i][j] means count for a i+1 - length string ending with j-th char
        # dp[j]  means count for a [1, n] - length string ending with j-th char
        dp = [1 for _ in range(5)]
        
        for i in range(1, n + 1):
            # ends with 'u'
            dp[4] = dp[0] + dp[1] + dp[2] + dp[3] + dp[4]
            # ends with 'o'
            dp[3] = dp[0] + dp[1] + dp[2] + dp[3]
            # ends with 'i'
            dp[2] = dp[0] + dp[1] + dp[2]            
            # ends with 'e'
            dp[1] = dp[0] + dp[1]
            # ends with 'a'
            dp[0] = dp[0]       
            
        print dp
        return dp[4]

'''
Your input
1
50
Your stdout
[1, 2, 3, 4, 5]
[1, 51, 1326, 23426, 316251]

Your answer
5
316251
Expected answer
5
316251
'''
