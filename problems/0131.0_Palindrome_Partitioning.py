'''
backtracking/DFS

Runtime: 941 ms, faster than 13.77% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.3 MB, less than 48.34% of Python3 online submissions for Palindrome Partitioning.
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def dfs(i, path):
            if i >= n:
                ans.append(path)
                return
            
            for j in range(i + 1, n + 1):
                if s[i: j] == s[i: j][:: -1]:
                    dfs(j, path + [s[i: j]])
        
        dfs(0, [])
        return ans 
    
'''
backtracking/DFS

Runtime: 1032 ms, faster than 9.16% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.4 MB, less than 34.74% of Python3 online submissions for Palindrome Partitioning.
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def dfs(i, path):
            if i >= n:
                ans.append(path)
                return
            
            for j in range(i + 1, n + 1):
                if s[i: j] == s[i: j][:: -1]:
                    path.append(s[i: j])
                    dfs(j, path[:])
                    path.pop()
                    
        dfs(0, [])
        return ans 

'''
backtracking/DFS

Runtime: 1058 ms, faster than 8.42% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.2 MB, less than 55.58% of Python3 online submissions for Palindrome Partitioning.
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def dfs(i, path):
            if i >= n:
                ans.append(path)
            
            for j in range(i + 1, n + 1):
                if s[i: j] == s[i: j][:: -1]:
                    path.append(s[i: j])
                    dfs(j, path[:])
                    path.pop()
                    
        dfs(0, [])
        return ans 
    

'''
backtracking with DP

Runtime: 1103 ms, faster than 7.05% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 30.6 MB, less than 20.92% of Python3 online submissions for Palindrome Partitioning.
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = []
        
        def dfs(i, path):
            if i >= n:
                ans.append(path)
            
            for j in range(i + 1, n + 1):
                # if s[i: j] == s[i: j][:: -1]:
                if s[i] == s[j - 1] and (j - i <= 2 or dp[i + 1][j - 2]):
                    dp[i][j - 1] = True
                    path.append(s[i: j])
                    dfs(j, path[:])
                    path.pop()
                    
        dfs(0, [])
        return ans 
    

