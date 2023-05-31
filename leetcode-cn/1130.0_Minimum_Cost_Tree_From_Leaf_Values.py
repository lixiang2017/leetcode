'''
执行用时：216 ms, 在所有 Python3 提交中击败了20.43% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了13.98% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        @cache
        def dfs(i, j):
            res = inf
            if i == j:
                return 0
            for k in range(i, j):
                l = dfs(i, k)
                r = dfs(k + 1, j)
                m = max(arr[i: k + 1]) * max(arr[k + 1: j + 1]) + l + r
                res = min(res, m)
            return res 

        return dfs(0, n - 1)
        