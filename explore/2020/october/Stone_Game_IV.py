'''
72 / 72 test cases passed.
Status: Accepted
Runtime: 3064 ms
Memory Usage: 17.1 MB
Submitted: 2 minutes ago
'''


class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # dp = [False] * (10 ** 5 + 5)
        # dp[:]
        
        #        0    1      2     3     4     5      6     7     8      9     10
        dp = [False, True, False, True, True, False, True, False, True, True, False]
        if n <= 10:
            return dp[n]
        
        for i in range(11, n + 1):
            j = 2  # j = 0
            while j * j <= i:
                j += 1
            if (j - 1) ** 2 == i:
                # dp[i] == True
                dp.append(True)
                continue
            k = j - 1
            can_win = False
            while k > 0:
                if dp[i - k ** 2] == False:
                    can_win = True
                    break
                    
                k -= 1
            dp.append(can_win)
            
        return dp[n]
            
                