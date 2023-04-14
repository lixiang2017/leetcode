'''
DFS + cache

Runtime: 953 ms, faster than 94.61% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 237.4 MB, less than 16.05% of Python3 online submissions for Longest Palindromic Subsequence.
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def longest_length(i: int, j: int) -> int:
            if i > j:
                return 0
            elif i == j:
                return 1
            if s[i] == s[j]:
                return 2 + longest_length(i + 1, j - 1)
            else:
                return max(longest_length(i, j - 1), longest_length(i + 1, j))
            
        return longest_length(0, len(s) - 1)


'''
1: 1 将递归翻译成递推
i or i+1 转移至 i, 所以 i 应该降序。 从 n-1 开始降序
j or j-1 转移至 j, 所以 j 应该升序。 从 i   开始升序
又 i <= j

Runtime: 1444 ms, faster than 61.19% of Python3 online submissions for Longest Palindromic Subsequence.
Memory Usage: 30.5 MB, less than 71.90% of Python3 online submissions for Longest Palindromic Subsequence.
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * (n) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    f[i][j] = 1
                elif s[i] == s[j]:
                    f[i][j] = 2 + f[i + 1][j - 1]
                else:
                    f[i][j] = max(f[i][j - 1], f[i + 1][j])
        
        return f[0][n - 1]

