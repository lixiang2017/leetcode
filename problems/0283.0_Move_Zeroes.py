'''
Author: lixiang
Beats: 94.68%
'''


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in nums:
            if n:
                nums[i] = n
                i += 1
        nums[i:] = [0] * (len(nums) - i)


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [1, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12]

    nums = [0, 0, 0, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == [0, 0, 0, 0, 0]

    nums = [4, 3, 2, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == [4, 3, 2, 0, 0]