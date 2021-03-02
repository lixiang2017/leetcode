'''
approach: Iteration, Layer by Layer
Time: O(M * N)
Space: O(M * N)

执行用时：32 ms, 在所有 Python 提交中击败了6.75%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了90.48%的用户
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        top, bottom, left, right = 0, M - 1, 0, N - 1
        while left <= right and top <= bottom:
            # add
            for j in range(left, right + 1):
                spiral.append(matrix[top][j])
            for i in range(top + 1, bottom + 1):
                spiral.append(matrix[i][right])
            if left < right and top < bottom:
                for j in range(right - 1, left - 1, -1):
                    spiral.append(matrix[bottom][j])
                for i in range(bottom - 1, top, -1):
                    spiral.append(matrix[i][left])

            left += 1
            top += 1
            right -= 1
            bottom -= 1

        return spiral




'''
approach: Simulation
Time: O(M * N)
Space: O(M * N)

执行用时：12 ms, 在所有 Python 提交中击败了91.47%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了26.39%的用户
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        visited = [[False] * N for _ in range(M)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total = M * N
        row = column = 0
        direction = 0
        for i in range(total):
            spiral.append(matrix[row][column])
            visited[row][column] = True
            nextRow = row + directions[direction][0]
            nextColumn = column + directions[direction][1]
            if not (0 <= nextRow < M and 0 <= nextColumn < N) or visited[nextRow][nextColumn]:
                direction = (direction + 1) % 4
            row += directions[direction][0]
            column += directions[direction][1]
        return spiral




'''
approach: DFS
Time: O(M * N)
Space: O(M * N), the length of stack will be max(M, N).

执行用时：16 ms, 在所有 Python 提交中击败了70.44%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了72.82%的用户
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        return self.dfs(matrix, 0, 0, M - 1, N - 1)
    
    def dfs(self, matrix, top, left, bottom, right):
        if top > bottom or left > right:
            return []
        spiral = []
        for j in range(left, right + 1):
            spiral.append(matrix[top][j])
        for i in range(top + 1, bottom + 1):
            spiral.append(matrix[i][right])
        if left < right and top < bottom:
            for j in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom][j])
            for i in range(bottom - 1, top, -1):
                spiral.append(matrix[i][left])
        
        return spiral + self.dfs(matrix, top + 1, left + 1, bottom - 1, right - 1)
    





