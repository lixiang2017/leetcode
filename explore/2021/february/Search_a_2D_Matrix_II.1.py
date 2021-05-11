'''
approach: Greedy
compare from top-right to bottom-left
Time: O(M + N), where M is the number of rows and N is the number of columns.
Space: O(1)

You are here!
Your runtime beats 80.42 % of python submissions.
You are here!
Your memory usage beats 22.01 % of python submissions.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        i , j = 0, N - 1
        while i < M and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


'''
approach: Greedy
compare from bottom-left to top-right 
Time: O(M + N), where M is the number of rows and N is the number of columns.
Space: O(1)

You are here!
Your runtime beats 64.51 % of python submissions.
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
        i , j = M - 1, 0
        while i >= 0 and j < N:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
                
        return False
    