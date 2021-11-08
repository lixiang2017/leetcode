'''
DFS

Runtime: 32 ms, faster than 67.01% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14.2 MB, less than 48.47% of Python3 online submissions for Unique Binary Search Trees.
'''
class Solution:
    def numTrees(self, n: int) -> int:
        # memo, range -> count
        memo = {0: 1, 1: 1}
        
        def construct(l: int, r: int) -> int:
            if r - l + 1 in memo:
                return memo[r - l + 1]

            total = 0
            for m in range(l, r + 1):
                cnt_l = construct(l, m - 1)
                cnt_r = construct(m + 1, r)
                total += cnt_l * cnt_r
            memo[r - l + 1] = total
            return total
              
        return construct(1, n)
         
'''
DFS

Runtime: 28 ms, faster than 86.81% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14.4 MB, less than 15.60% of Python3 online submissions for Unique Binary Search Trees.
'''
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def G(n):
            if n == 0:
                return 1
            return sum(G(i) * G(n - i - 1) for i in range(n))
        return G(n)
