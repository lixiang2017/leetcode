'''
You are here!
Your runtime beats 31.14 % of python submissions.
'''

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calculate_digits(num):
            if not num:
                return 1
            
            digits = 0
            while num:
                num /= 10
                digits += 1
            
            return digits
        
        return sum([(calculate_digits(num) & 1 ) == 0 for num in nums])

