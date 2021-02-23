'''
approach: Binary Search Row by Row
Time: O(M * logN), where M is the number of rows and N is the number of columns.
Space: O(1)

You are here!
Your runtime beats 22.08 % of python submissions.
You are here!
Your memory usage beats 51.46 % of python submissions.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[M - 1][N - 1]:
            return False
        
        for i in range(M):
            if target < matrix[i][0]:
                return False
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right) / 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


'''
approach: Binary Search Row by Row
Time: O(M * logN), where M is the number of rows and N is the number of columns.
Space: O(1)

You are here!
Your runtime beats 64.51 % of python submissions.
You are here!
Your memory usage beats 77.71 % of python submissions.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[M - 1][N - 1]:
            return False
        
        for i in range(M):
            if target < matrix[i][0]:
                return False
            if target > matrix[i][N - 1]:   # optimize
                continue
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right) / 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
    