'''
approach: Sum
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 97.92 % of python submissions.
You are here!
Your memory usage beats 73.39 % of python submissions.
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (1 + n) / 2 - sum(nums)



'''
approach: XOR
Time: O(N)
Space: O(1)
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    