'''
记得加  @cache

Runtime: 70 ms, faster than 45.60% of Python3 online submissions for Interleaving String.
Memory Usage: 15.7 MB, less than 9.82% of Python3 online submissions for Interleaving String.

如果不加 @cache，会超时

93 / 106 test cases passed.
    Status: Time Limit Exceeded
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False 
        
        @cache
        def dfs(i, j, k):
            if i == m and j == n:
                return True 
            check = False 
            if i < m and s1[i] == s3[k]:
                check |= dfs(i + 1, j, k + 1)
            if j < n and s2[j] == s3[k]:
                check |= dfs(i, j + 1, k + 1)
            return check
        
        return dfs(0, 0, 0)
                

'''
DFS + memoization

Runtime: 95 ms, faster than 16.55% of Python3 online submissions for Interleaving String.
Memory Usage: 15.8 MB, less than 7.14% of Python3 online submissions for Interleaving String.
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, o = len(s1), len(s2), len(s3)
        if m + n != o:
            return False 
        
        memo = {}
        def dfs(i, j, k):
            if i == m and j == n:
                return True 
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            check = False 
            if i < m and s1[i] == s3[k]:
                check |= dfs(i + 1, j, k + 1)
            if j < n and s2[j] == s3[k]:
                check |= dfs(i, j + 1, k + 1)
            memo[(i, j, k)] = check
            return check
        
        return dfs(0, 0, 0)
                


