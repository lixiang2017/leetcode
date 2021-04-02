'''
approach: Binary Search
Time: O(log(MN))
Space: O(1)

执行用时：20 ms, 在所有 Python 提交中击败了62.77%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了34.93%的用户
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        left, right = 0, M * N - 1
        while left <= right:
            mid = (right - left) / 2 + left
            cur = matrix[mid / N][mid % N]
            if cur == target:
                return True
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1
        return False



'''
approach: Binary Search
Time: O(log(M) + log(N)) = O(log(MN))
Space: O(1)

执行用时：20 ms, 在所有 Python 提交中击败了62.77%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了28.19%的用户
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        rowIdx = self.binarySearchFirstColumn(matrix, M, target)
        if rowIdx < 0:
            return False
        return self.binarySearchRow(matrix, rowIdx, N, target)

    def binarySearchFirstColumn(self, matrix, M, target):
        low, high = -1, M - 1
        while low < high:
            # mid = (high - low) / 2 + low  # wrong
            mid = (high - low + 1) / 2 + low
            cur = matrix[mid][0]
            if cur <= target:
                low = mid
            else:
                high = mid - 1
        return low
    
    def binarySearchRow(self, matrix, rowIdx, N, target):
        left, right = 0, N - 1
        while left <= right:
            mid = (right - left) / 2 + left
            cur = matrix[rowIdx][mid]
            if cur == target:
                return True
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

'''
[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
13
'''
