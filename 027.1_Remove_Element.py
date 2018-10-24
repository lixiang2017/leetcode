'''
Author: lixiang
Beats: 99.66%
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)

if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val))

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(Solution().removeElement(nums, val))