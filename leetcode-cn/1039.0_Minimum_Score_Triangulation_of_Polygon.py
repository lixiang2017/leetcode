'''
区间DP
https://www.bilibili.com/video/BV1Gs4y1E7EU/

执行用时：128 ms, 在所有 Python3 提交中击败了23.08% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了10.25% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = inf
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
            return res
        
        return dfs(0, len(values) - 1)
        

'''
DP

执行用时：100 ms, 在所有 Python3 提交中击败了74.36% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了75.64% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                f[i][j] = inf
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + values[i] * values[j] * values[k])
        return f[0][n - 1]


'''
DP
res

执行用时：92 ms, 在所有 Python3 提交中击败了88.46% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了70.51% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                res = inf
                for k in range(i + 1, j):
                    res = min(res, f[i][k] + f[k][j] + values[i] * values[j] * values[k])
                f[i][j] = res
        return f[0][n - 1]

