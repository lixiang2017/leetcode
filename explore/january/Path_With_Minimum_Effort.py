'''
approach: Binary Search + BFS

Time: O(log(10^6) * M * N)
Space: O(M * N)

You are here!
Your runtime beats 16.74 % of python submissions.
You are here!
Your memory usage beats 92.31 % of python submissions.
'''


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        effort = 999999
        left, right = 0, 999999
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while left <= right:
            mid = (left + right) / 2
            q = []
            q.append([0, 0]) # the top-left point
            seen = [[0 for _ in range(n)] for _ in range(m)]
            seen[0][0] = 1
            while q:
                x, y = q.pop(0)
                for deltax, deltay in directions:
                    nx = x + deltax
                    ny = y + deltay
                    if (nx >= 0 and nx < m and ny >= 0 and ny < n and not seen[nx][ny] \
                       and abs(heights[x][y] - heights[nx][ny]) <= mid):
                        q.append([nx, ny])
                        seen[nx][ny] = 1
                        
            if seen[m - 1][n - 1]:
                effort = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return effort
    