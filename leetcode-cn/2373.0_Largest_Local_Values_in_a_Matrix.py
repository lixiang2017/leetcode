'''
brute force

执行用时：112 ms, 在所有 Python3 提交中击败了30.99% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了7.02% 的用户
通过测试用例：50 / 501
'''
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                ans[i - 1][j - 1] = max(grid[i + di][j +dj] for di in range(-1, 2) for dj in range(-1, 2))
        return ans

