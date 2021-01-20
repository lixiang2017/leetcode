'''
approach: Dynamic Programming
Time: O(N)
Space: O(1)

ref:
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Success
Details
Runtime: 44 ms, faster than 88.34% of Python online submissions for Maximum Subarray.
Memory Usage: 14.5 MB, less than 23.51% of Python online submissions for Maximum Subarray.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = current_sum = -1e5 - 2
        for num in nums:
            current_sum = max(current_sum + num, num)
            best_sum = max(current_sum, best_sum)
            
        return best_sum
        