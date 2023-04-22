'''
DFS + memo

Runtime: 875 ms, faster than 63.29% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
Memory Usage: 167.2 MB, less than 14.61% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
'''
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        
        @cache
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return 1 + min(dfs(i, j - 1), dfs(i + 1, j))
        
        return dfs(0, n - 1)
        

'''
DP

Runtime: 606 ms, faster than 92.29% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
Memory Usage: 16.3 MB, less than 37.93% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
'''
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1]
                else:
                    f[i][j] = 1 + min(f[i][j - 1], f[i + 1][j]) 
        return f[0][n - 1]

        
