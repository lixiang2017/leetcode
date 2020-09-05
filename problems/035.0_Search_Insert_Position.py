'''
Time:  O(n)
Space: O(1)

Solution: linear search / sequential search
Author: lixiang
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return i + 1

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