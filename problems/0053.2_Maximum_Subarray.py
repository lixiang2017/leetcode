'''
approach: Dynamic Programming
Time: O(N)
Space: O(1)

ref:
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Success
Details
Runtime: 48 ms, faster than 70.13% of Python online submissions for Maximum Subarray.
Memory Usage: 14.5 MB, less than 16.16% of Python online submissions for Maximum Subarray.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = -1e5 - 2
        for num in nums:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far
        