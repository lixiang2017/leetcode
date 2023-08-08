'''
Success
Details
Runtime: 28 ms, faster than 61.59% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.9 MB, less than 12.79% of Python online submissions for Search in Rotated Sorted Array.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        for i in range(size):
            if nums[i] == target:
                return i      

        return -1



'''
binary search
T: O(logN)
S: O(1)
Runtime: 54 ms, faster than 64.87% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 16.7 MB, less than 72.11% of Python3 online submissions for Search in Rotated Sorted Array.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # Case 1: find target
            if nums[mid] == target:
                return mid
            
            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                
            # Case 3: subarray on mid's right is sorted.
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return -1



