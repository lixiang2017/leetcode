'''
DP, T: O(N^2), S: O(N^2)
执行用时：7448 ms, 在所有 Python3 提交中击败了13.19% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了14.03% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s 

        dp = [[False] * n for _ in range(n)]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
        
        for L in range(2, n + 1):
            # start
            for i in range(n):
                # end  # L = j - i + 1
                j = L + i - 1
                if j >= n:
                    break
                
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and L > len(ans):
                    ans = s[i: j + 1]

        return ans 

'''
执行用时：6948 ms, 在所有 Python3 提交中击败了24.83% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了21.74% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s 

        dp = [[False] * n for _ in range(n)]
        begin, max_len = 0, 1
        for i in range(n):
            dp[i][i] = True
        
        for L in range(2, n + 1):
            # start
            for i in range(n):
                # end  # L = j - i + 1
                j = L + i - 1
                if j >= n:
                    break
                
                if s[i] != s[j]:
                    dp[i][j] = False
                elif j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and L > max_len:
                    max_len = L 
                    begin = i 

        return s[begin: begin + max_len] 


'''
T: O(N^2), S: O(1)
执行用时：820 ms, 在所有 Python3 提交中击败了68.34% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了78.88% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def expandAroundCenter(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i + 1, j - 1
        
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1 
            if right2 - left2 > end - start:
                start, end = left2, right2 
        return s[start: end + 1]

