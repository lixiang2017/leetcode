'''
The most important observation is the "if nums[mid] and target are "on the same side" of nums[0], just take nums[mid] "

You are here!
Your runtime beats 31.16 % of python submissions.
'''



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid
            elif target > nums[mid]:
                hi = mid - 1
            else: # target < nums[mid]
                lo = mid + 1
        
        return -1