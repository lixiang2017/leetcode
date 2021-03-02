'''
You are here!
Your runtime beats 97.00 % of python submissions.
'''


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_digits_count = 0
        for num in nums:
            if 10 ** 1 <= num and num < 10 ** 2:
                even_digits_count += 1
            elif 10 ** 3 <= num and num < 10 ** 4:
                even_digits_count += 1
            elif 10 ** 5 <= num:
                even_digits_count += 1
        
        return even_digits_count
        