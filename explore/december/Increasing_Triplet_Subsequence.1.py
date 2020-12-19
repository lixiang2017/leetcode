'''
You are here!
Your runtime beats 37.96 % of python submissions.

Time: O(N)
Space: O(1)
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = sys.maxint
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False
