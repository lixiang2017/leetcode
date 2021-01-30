'''
approach: Binary Search + DFS
Time: O(log(N ^ 2) * N ^ 2) = O(N ^ 2 * logN)
Space: O(N ^ 2 + N ^ 2) = O(N ^ 2)

same as https://leetcode-cn.com/problems/path-with-minimum-effort/

执行结果：
通过
显示详情
执行用时：128 ms, 在所有 Python 提交中击败了53.85%
的用户
内存消耗：15.1 MB, 在所有 Python 提交中击败了11.54%的用户
'''


class Solution(object):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        least = -1
        size = len(grid)
        left, right = 0, size * size - 1
        left = max(grid[0][0], grid[size - 1][size - 1])
        
        while left <= right:
            mid = left + (right - left) / 2
            seen = [0 for _ in range(size * size)]

            if self.dfs(0, 0, size, seen, grid, mid):
                least = mid
                right = mid - 1
            else:
                left = mid + 1

        return least
    
    def dfs(self, startx, starty, size, seen, grid, mid):
        if startx == size - 1 and starty == size - 1: return True
        seen[startx * size + starty] = 1

        for deltax, deltay in self.directions:
            nx, ny = startx + deltax, starty + deltay
            if nx >= 0 and nx < size and ny >= 0 and ny < size and \
                    not seen[nx * size + ny] and grid[nx][ny] <= mid:
                if self.dfs(nx, ny, size, seen, grid, mid):
                    return True
        
        return False
