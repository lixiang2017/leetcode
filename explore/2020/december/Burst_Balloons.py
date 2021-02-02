'''
use functools.lru_cache in python3

You are here!
Your runtime beats 58.39 % of python3 submissions.
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import lru_cache
        A = [1] + nums + [1]
        
        @lru_cache(None)
        def dfs(i, j):
            return max([A[i] * A[k] * A[j] + dfs(i, k) + dfs(k, j) for k in range(i + 1, j)] or [0])
        
        return dfs(0, len(A) - 1)        
