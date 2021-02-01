'''
approach: Gredy + Heap

You are here!
Your memory usage beats 77.05 % of python submissions.

ref:
https://leetcode-cn.com/problems/minimize-deviation-in-array/solution/xian-ba-qi-shu-bian-ou-shu-by-lucien_z/
'''

import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # minValue = min(nums)   # wrong
        nums = [-2 * num if num & 1 else -num for num in nums]
        minValue = - max(nums)
        heapq.heapify(nums)
        
        diff = -nums[0] - minValue
        while ~ nums[0] & 1:   # 按位取反
            half = nums[0] >> 1
            # half = nums[0] // 2
            if -half <  minValue:
                minValue = -half
                
            heapq.heapreplace(nums, half)
            diff = min(diff, -nums[0] - minValue)
        
        return diff
    