'''
approach: Binary Search + DFS


You are here!
Your runtime beats 21.27 % of python submissions.
You are here!
Your memory usage beats 18.55 % of python submissions.
'''


class Solution(object):
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        effort = -1
        left, right = 0, 999999
 
        while left <= right:
            # print 'left, right: ', left, right
            mid = (left + right) / 2
            seen = [[0 for _ in range(n)] for _ in range(m)]

            if self.dfs(heights, seen, 0, 0, m, n, mid):
                effort = mid
                right = mid - 1
            else:
                left = mid + 1

        return effort

    def dfs(self, heights, seen, x, y, m, n, effort):
        if x == m - 1 and y == n - 1: return True
        if seen[x][y]: return False
        seen[x][y] = 1
        for deltax, deltay in self.directions:
            nx = x + deltax
            ny = y + deltay
            if (nx >= 0 and nx < m and ny >= 0 and ny < n and not seen[nx][ny] \
                       and abs(heights[x][y] - heights[nx][ny]) <= effort):
                if self.dfs(heights, seen, nx, ny, m, n, effort):
                    return True
                
        return False

'''
Your input
[[1,2,2],[3,8,2],[5,3,5]]
Your stdout
left, right:  0 999999
left, right:  0 499998
left, right:  0 249998
left, right:  0 124998
left, right:  0 62498
left, right:  0 31248
left, right:  0 15623
left, right:  0 7810
left, right:  0 3904
left, right:  0 1951
left, right:  0 974
left, right:  0 486
left, right:  0 242
left, right:  0 120
left, right:  0 59
left, right:  0 28
left, right:  0 13
left, right:  0 5
left, right:  0 1
left, right:  1 1
Your answer
2
Expected answer
2
'''

