'''
You are here!
Your runtime beats 98.72 % of python submissions.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size= len(nums)
        left, right = 0, size - 1
        
        while left <= right:   # '<' will be Wrong Answer for input: [5] 5
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1