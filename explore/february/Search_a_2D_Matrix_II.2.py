'''
approach: Binary Search, according the diagonal line
Time: O(log(N!))
Space: O(1)

ref:
https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/

You are here!
Your runtime beats 7.29 % of python submissions.
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
        
        for i in range(min(M, N)):
            vertical_found = self.binarySearch(matrix, target, i, True)
            horizontal_found = self.binarySearch(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        return False
    
    def binarySearch(self, matrix, target, start, isVertical):
        lo = start
        hi = len(matrix) - 1 if isVertical else len(matrix[0]) - 1
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if isVertical:  # search a column
                if matrix[mid][start] == target:
                    return True
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1     
            else: # search a row
                if matrix[start][mid] == target:
                    return True
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1               
        
        return False




'''
approach: Recursion
Time: O(N*logN)
Space:O(logN)

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
        def searchRecursive(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left) / 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return searchRecursive(left, row, mid - 1, down) or searchRecursive(mid + 1, up, right, row - 1)
        
        
        return searchRecursive(0, 0, len(matrix[0]) - 1, len(matrix) - 1)

