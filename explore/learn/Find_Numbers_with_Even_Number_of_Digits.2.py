'''
Submission Result: Wrong Answer 
Input: [12,345,2,6,7896]
Output: 0
Expected: 2
'''


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([(len(str(num)) | 0) == 0 for num in nums])
        # cause 2 | 0 will be 2, not 0