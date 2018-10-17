'''
Solution: bisect module
Author: lixiang
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        return bisect.bisect_left(nums, target)


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