'''

执行用时：24 ms, 在所有 Python 提交中击败了87.79%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了94.97%的用户
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
        while left <= right and top <= bottom:
            # left to right
            for j in range(left, right + 1):
                spiral.append(matrix[top][j])
            # right to bottom
            for i in range(top + 1, bottom + 1):
                spiral.append(matrix[i][right])
            if left < right and top < bottom:
                # right to left
                for j in range(right - 1, left - 1, -1):
                    spiral.append(matrix[bottom][j])
                # bottom to top
                for i in range(bottom - 1, top, -1):
                    spiral.append(matrix[i][left])
            top += 1
            left += 1
            right -= 1
            bottom -= 1

        return spiral



'''
逆时针旋转 == （转置+倒序)
转置: zip
倒序: [:: -1]

执行用时：36 ms, 在所有 Python 提交中击败了36.27%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了9.69%的用户
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        while matrix:
            spiral.extend(matrix[0])
            matrix = zip(*matrix[1:])[::-1]
        return spiral
