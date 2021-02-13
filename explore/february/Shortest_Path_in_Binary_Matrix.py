'''
approach: BFS
Time: O(N * N)
Space: O(N)

You are here!
Your runtime beats 76.47 % of python submissions.
You are here!
Your memory usage beats 57.84 % of python submissions.
'''


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size = len(grid)
        q = [(0, 0, 1)]  # (x, y, steps)
        seen = [0 for _ in range(size * size)]
        if grid[0][0] == 0:
            seen[0] = 1
        else:
            return -1
        directions = [(-1, -1), (0, -1), (1, -1),
                     (-1, 0), (0, 0), (1, 0),
                     (-1, 1), (0, 1), (1, 1)]
        
        while q:
            x, y, steps = q.pop(0)
            if seen[size * size - 1]:
                return steps
            for deltax, deltay in directions:
                newx, newy = x + deltax, y + deltay
                if newx >= 0 and newx < size and newy >= 0 and newy < size and \
                        grid[newx][newy] == 0 and not seen[newx * size + newy]:
                    q.append((newx, newy, steps + 1))
                    seen[newx * size + newy] = 1

        return -1
