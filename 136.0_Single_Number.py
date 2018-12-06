class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


if __name__ == "__main__":
    nums = [2, 2, 1]
    assert Solution().singleNumber(nums) == 1

    nums = [4, 1, 2, 1, 2]
    assert Solution().singleNumber(nums) == 4

    nums = [5]
    assert Solution().singleNumber(nums) == 5
