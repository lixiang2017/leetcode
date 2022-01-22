'''
Runtime: 399 ms, faster than 82.63% of Python3 online submissions for Stone Game IV.
Memory Usage: 18.9 MB, less than 43.71% of Python3 online submissions for Stone Game IV.
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(None)
        def dfs(remain):
            if not remain:
                return False
            return any(not dfs(remain - k * k) for k in range(1, int(sqrt(remain)) + 1)[:: -1])
        
        return dfs(n)
        