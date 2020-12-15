'''
approach: merge sort

You are here!
Your runtime beats 8.40 % of python submissions.
'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        
        squares = [num * num for num in nums]
        minimum_index = 0
        minimum = squares[0]
        size = len(squares)
        for i in range(size):
            if squares[i] < minimum:
                minimum = squares[i]
                minimum_index = i
                
        # merge sort
        left = squares[:minimum_index][:: -1]
        right = squares[minimum_index:]
        sorted_squares = []
        while left and right:
            if left[0] < right[0]:
                sorted_squares.append(left.pop(0))
            elif left[0] > right[0]:
                sorted_squares.append(right.pop(0))
            else:
                sorted_squares.append(left.pop(0))
                sorted_squares.append(right.pop(0))
        if left:
            sorted_squares.extend(left)
        if right:
            sorted_squares.extend(right)
        return sorted_squares
            