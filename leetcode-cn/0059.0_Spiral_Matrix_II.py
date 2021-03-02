'''
approach: Layer by Layer
Time: O(N * N)
Space: O(N * N)

执行用时：8 ms, 在所有 Python 提交中击败了98.46%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.25%的用户
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        left = top = 0
        right = bottom = n - 1
        idx = 1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                matrix[top][j] = idx
                idx += 1
            for i in range(top + 1, bottom + 1):
                matrix[i][right] = idx
                idx += 1
            
            for j in range(right - 1, left - 1, -1):
                matrix[bottom][j] = idx
                idx += 1
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = idx
                idx += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            
        return matrix


'''
approach: Simulation
Time: O(N * N)
Space: O(N * N)

执行用时：20 ms, 在所有 Python 提交中击败了53.85%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了61.73%的用户
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        # seen = [[False] * n for _ in range(n)]  # no need
        left = top = 0
        right = bottom = n - 1
        idx, total = 1, n * n
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = column = 0
        direct = 0
        while idx <= total:
            matrix[row][column] = idx
            idx += 1
            nextRow = row + directions[direct][0]
            nextColumn = column + directions[direct][1]
            if not (0 <= nextRow < n and 0 <= nextColumn < n) or matrix[nextRow][nextColumn]:
                direct = (direct + 1) % 4
            row += directions[direct][0]
            column += directions[direct][1]
    
        return matrix
