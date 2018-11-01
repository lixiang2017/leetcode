'''
Author: lixiang
Beats: 57.99% --> 22.38% --> 46.55% --> 57.99%
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num = nums[0]
        i = 1
        while i < len(nums):
            if num == nums[i]:
                del nums[i]
            else:
                num = nums[i]
                i += 1

        return len(nums)

if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates((nums)))

    nums = [2]
    print(Solution().removeDuplicates(nums))
