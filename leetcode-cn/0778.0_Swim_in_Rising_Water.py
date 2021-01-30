'''
approach: Binary Search + BFS
Time: O(log(N ^ 2) * N ^ 2) = O(N ^ 2 * logN)
Space: O(N ^ 2 + N ^ 2) = O(N ^ 2)

same as https://leetcode-cn.com/problems/path-with-minimum-effort/
执行结果：
通过
显示详情
执行用时：152 ms, 在所有 Python 提交中击败了50.00%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了96.15%的用户
'''


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        least = -1
        n = len(grid)
        left, right = 0, n * n - 1
        left = max(grid[0][0], grid[n - 1][n - 1])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while left <= right:
            mid = (left + right) / 2
            q = [[0, 0]] # beginning
            seen = [0 for _ in range(n * n)]
            seen[0] = 1
            while q:
                x, y = q.pop(0)
                for deltax, deltay in directions:
                    nx, ny = x + deltax, y + deltay
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and not seen[nx * n + ny] \
                            and grid[nx][ny] <= mid:
                        q.append([nx, ny])
                        seen[nx * n + ny] = 1

            if seen[n * n - 1]:
                least = mid
                right = mid - 1
            else:
                left = mid + 1

        return least
