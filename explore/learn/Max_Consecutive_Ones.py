'''
You are here!
Your runtime beats 99.75 % of python submissions.
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_consecutive = 0
        
        consecutive = 0
        for num in nums:    
            if num:
                consecutive += 1
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
            else:
                consecutive = 0
        
        return max_consecutive
            