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

'''
DP

Runtime: 5564 ms, faster than 28.57% of Python3 online submissions for Maximum Value of K Coins From Piles.
Memory Usage: 14.4 MB, less than 86.96% of Python3 online submissions for Maximum Value of K Coins From Piles.
'''
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        f = [0] * (k + 1)
        
        for pile in piles:
            n = len(pile)
            for i in range(1, n):
                pile[i] += pile[i - 1]
          
            for j in range(k, 0, -1):
                for w in range(min(n, j)):
                    f[j] = max(f[j], f[j - w - 1] + pile[w])
        
        return f[k]       



'''
ref:
https://leetcode.cn/problems/maximum-value-of-k-coins-from-piles/solution/zhuan-hua-cheng-fen-zu-bei-bao-pythongoc-3xnk/


Runtime: 3898 ms, faster than 96.27% of Python3 online submissions for Maximum Value of K Coins From Piles.
Memory Usage: 14.4 MB, less than 97.52% of Python3 online submissions for Maximum Value of K Coins From Piles.
'''
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        f = [0] * (k + 1)
        sum_n = 0
        for pile in piles:
            n = len(pile)
            for i in range(1, n):
                pile[i] += pile[i - 1]  # pile 前缀和
            sum_n = min(sum_n + n, k)   # 优化：j 从前 i 个栈的大小之和开始枚举（不超过 k）
            for j in range(sum_n, 0, -1):
                for w in range(min(n, j)):
                    f[j] = max(f[j], f[j - w - 1] + pile[w])
        
        return f[k]        




