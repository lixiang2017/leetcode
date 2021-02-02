'''
approach: merge sort

You are here!
Your runtime beats 10.15 % of python submissions.
'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        
        # squares = [num * num for num in nums]
        squares = []
        minimum_index = 0
        # minimum = abs(nums[0])
        minimum = nums[0] * nums[0]
        size = len(nums)
        for i in range(size):
            squares.append(nums[i] * nums[i])
            if squares[-1] < minimum:
                minimum = squares[-1]
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
            