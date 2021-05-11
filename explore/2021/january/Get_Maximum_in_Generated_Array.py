'''
Time: O(N)
Space:O(N)

You are here!
Your runtime beats 80.00 % of python submissions.
You are here!
Your memory usage beats 66.47 % of python submissions.
'''


class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1]
        if n <= 1: return nums[n]
        
        maximum = 1
        for i in range(1, n / 2):
            nums.append(nums[i])
            nums.append(nums[i] + nums[i + 1])
            maximum = max(maximum, nums[i], nums[i] + nums[i + 1])
        
        nums.append(nums[n / 2])
        maximum = max(maximum, nums[-1])
        if n & 1:
            nums.append(nums[n / 2] + nums[n / 2 + 1])
            maximum = max(maximum, nums[-1])
        
        return maximum
