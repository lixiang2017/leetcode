'''
Runtime: 1509 ms, faster than 11.37% of Python3 online submissions for Extra Characters in a String.
Memory Usage: 18.2 MB, less than 13.23% of Python3 online submissions for Extra Characters in a String.
'''
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        library = set(dictionary)
        ans = n
        
        @cache
        def dfs(i, extra):
            nonlocal ans
            if i >= n:
                ans = min(ans, extra)
                return 
            for j in range(i + 1, n + 1):
                if s[i: j] in library:
                    dfs(j, extra)
                else:
                    dfs(j, extra + j - i)
        
        dfs(0, 0)
        return ans 
        
        