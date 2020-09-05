'''
Author: lixiang
Beats: 21.43%
'''

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        return sorted(nums).index(target)

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 0
    print(Solution().searchInsert(nums, target))