'''
Success
Details
Runtime: 60 ms, faster than 50.63% of Python online submissions for Minimum Subsequence in Non-Increasing Order.
Memory Usage: 13.2 MB, less than 16.74% of Python online submissions for Minimum Subsequence in Non-Increasing Order.
'''

class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all_sum = sum(nums)
        nums.sort(reverse=True)
        
        sub_sum = 0
        subsequence = []
        for num in nums:
            subsequence.append(num)   # the two lines need to put before if statement
            sub_sum += num            
            
            if sub_sum > all_sum - sub_sum:
                return subsequence
