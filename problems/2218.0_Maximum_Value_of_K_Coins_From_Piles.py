'''
DFS + memo + prefix sum
分组背包

Runtime: 5243 ms, faster than 35.22% of Python3 online submissions for Maximum Value of K Coins From Piles.
Memory Usage: 139.7 MB, less than 44.65% of Python3 online submissions for Maximum Value of K Coins From Piles.
'''
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        presums = [[0] + list(accumulate(p)) for p in piles]
        n = len(piles)
        
        @cache
        def dfs(idx, r):
            if idx == n or r < 0:
                return 0
            return max(dfs(idx + 1, r - take) + presums[idx][take] for take in range(min(len(piles[idx]), r) + 1))
        
        return dfs(0, k)

'''
Runtime: 4942 ms, faster than 39.00% of Python3 online submissions for Maximum Value of K Coins From Piles.
Memory Usage: 139.7 MB, less than 44.65% of Python3 online submissions for Maximum Value of K Coins From Piles.
'''
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        presums = [[0] + list(accumulate(p)) for p in piles]
        n = len(piles)
        
        @cache
        def dfs(idx, r):
            return max(dfs(idx + 1, r - take) + presums[idx][take] for take in range(min(len(piles[idx]), r) + 1)) if idx < n and r else 0
        
        return dfs(0, k)
        

'''
Runtime: 4986 ms, faster than 38.37% of Python3 online submissions for Maximum Value of K Coins From Piles.
Memory Usage: 139.8 MB, less than 44.65% of Python3 online submissions for Maximum Value of K Coins From Piles.
'''
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        presums, n = [[0] + list(accumulate(p)) for p in piles], len(piles)
        
        @lru_cache(None)
        def dfs(idx, r):
            return max(dfs(idx + 1, r - i) + presums[idx][i] for i in range(min(r, len(piles[idx])) + 1)) if idx < n and r else 0
        
        return dfs(0, k)

'''
作者：himymBen
链接：https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/solution/-by-himymben-qzs2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

