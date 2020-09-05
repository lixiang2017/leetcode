'''
Time:  O(logn)
Space: O(1)

Solution: binary search
Author: lixiang
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))

    target = 2
    print(Solution().searchInsert(nums, target))

    target = 7
    print(Solution().searchInsert(nums, target))

    target = 0
    print(Solution().searchInsert(nums, target))