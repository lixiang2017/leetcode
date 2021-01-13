'''
Hint 1: Find the minimum prefix sum.

Time: O(N)
Space: O(1)

Success
Details 
Runtime: 16 ms, faster than 85.56% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 13.2 MB, less than 92.78% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
'''


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixSum = 0
        minPrefixSum = sys.maxint
        
        for num in nums:
            prefixSum += num
            minPrefixSum = min(minPrefixSum, prefixSum)
        
        return 1 if minPrefixSum >= 0 else - minPrefixSum + 1
