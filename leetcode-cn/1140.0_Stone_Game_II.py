'''
cache

执行用时：124 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了55.00% 的用户
通过测试用例：92 / 92
'''
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [piles[-1]] * n
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        @cache
        def dfs(i, m):
            if i + 2 * m >= n:
                return suffix_sum[i]
            return suffix_sum[i] - min(dfs(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        
        return dfs(0, 1)
