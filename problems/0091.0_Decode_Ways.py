'''
DP
T: O(N)
S: O(N)

Runtime: 51 ms, faster than 61.27% of Python3 online submissions for Decode Ways.
Memory Usage: 13.9 MB, less than 80.35% of Python3 online submissions for Decode Ways.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1, 1] + [0] * n
        for i, ch in enumerate(s):
            # just single ch
            if ch != '0':
                dp[i + 2] = dp[i + 1]
            # s[i-1] and ch 
            if i > 0:
                if (s[i - 1] == '1') or (s[i - 1] == '2' and ord(ch) <= ord('6')):
                    dp[i + 2] += dp[i]
        return dp[-1]
        
