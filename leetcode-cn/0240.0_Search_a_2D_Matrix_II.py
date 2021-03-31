'''
approach: Greedy
Time: O(M + N)
Space: O(1)

执行用时：160 ms, 在所有 Python 提交中击败了31.30%的用户
内存消耗：18.8 MB, 在所有 Python 提交中击败了87.58%的用户
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        # start from bottom left
        i, j = M - 1, 0
        while i >= 0 and j < N:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                i -= 1
            else:
                j += 1
        return False



'''
approach: Greedy
Time: O(M + N)
Space: O(1)

执行用时：144 ms, 在所有 Python 提交中击败了88.20%的用户
内存消耗：18.8 MB, 在所有 Python 提交中击败了89.57%的用户
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        # start from top right
        i, j = 0, N - 1
        while i < M and j >= 0:
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                j -= 1
            else:
                i += 1
        return False

'''
approach: Brute Force
Time: O(MN)
Space: O(1)

执行用时：160 ms, 在所有 Python 提交中击败了31.30%的用户
内存消耗：19 MB, 在所有 Python 提交中击败了38.51%的用户
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target in row:
                return True         
        return False
        


