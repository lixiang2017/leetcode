'''
prefix sum

执行用时：332 ms, 在所有 Python3 提交中击败了15.13% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了48.74% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # prefix sum
        horizontal, vertical = deepcopy(grid), deepcopy(grid)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if j > 0:
                        horizontal[i][j] = horizontal[i][j - 1] + 1
                    if i > 0:
                        vertical[i][j] = vertical[i - 1][j] + 1
        max_edge = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                # edge length
                for e in range(max_edge + 1, min(m, n) + 1):
                    if i + e > m or j + e > n:
                        break 
                    # from top-left i,j to bottom-right i+e-1,j+e-1
                    b, r = i + e - 1, j + e - 1
                    if horizontal[i][r] - horizontal[i][j] == e - 1 and \
                        horizontal[b][r] - horizontal[b][j] == e - 1 and \
                        vertical[b][j] - vertical[i][j] == e - 1 and \
                        vertical[b][r] - vertical[i][r] == e - 1:
                        max_edge = max(max_edge, e)
        return max_edge * max_edge 

