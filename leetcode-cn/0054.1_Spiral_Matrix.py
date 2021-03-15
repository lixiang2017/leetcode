'''
approach: Iteration
Time: O(M * N)
Space: O(M * N)

执行用时：12 ms, 在所有 Python 提交中击败了91.41%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了87.80%的用户
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        top, left, bottom, right = 0, 0, M - 1, N - 1
        spiral = []
        while top <= bottom and left <= right:
            # from left to right
            for j in range(left, right + 1):
                spiral.append(matrix[top][j])
            # from top to bottom
            for i in range(top + 1, bottom + 1):
                spiral.append(matrix[i][right])
            if top < bottom and left < right:
                # from right to left
                for j in range(right - 1, left - 1, -1):
                    spiral.append(matrix[bottom][j])
                # from bottom to top
                for i in range(bottom - 1, top, -1):
                    spiral.append(matrix[i][left])

            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return spiral
