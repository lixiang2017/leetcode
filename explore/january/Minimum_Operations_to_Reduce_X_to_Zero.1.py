'''
approach: Sliding Window / Two Pointers

You are here!
Your runtime beats 44.98 % of python submissions.
You are here!
Your memory usage beats 83.39 % of python submissions.
'''

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        maxPart = -1
        all_sum = sum(nums)
        currentSum = left = right = 0
        
        while left < len(nums):
            
            if right < len(nums):
                currentSum += nums[right]
                right += 1
            
            while (currentSum > all_sum - x and left < len(nums)):
                currentSum -= nums[left]
                left += 1
            if currentSum == all_sum - x:
                maxPart = max(maxPart, right - left)
            
            if right == len(nums):
                left += 1
            
        return -1 if maxPart == -1 else len(nums) - maxPart
