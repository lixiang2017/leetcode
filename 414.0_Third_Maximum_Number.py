'''
Success
Details 
Runtime: 28 ms, faster than 99.43% of Python online submissions for Third Maximum Number.
Memory Usage: 13 MB, less than 25.00% of Python online submissions for Third Maximum Number.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


if __name__ == "__main__":
    nums = [3, 2, 1]
    assert Solution().thirdMax(nums) == 1

    nums = [1, 2]
    assert Solution().thirdMax(nums) == 2

    nums = [2, 2, 3, 1]
    assert Solution().thirdMax(nums) == 1

    nums = [5]
    assert Solution().thirdMax(nums) == 5

    nums = [6, 6, 6]
    assert Solution().thirdMax(nums) == 6

    nums = [6, 6, 7]
    assert Solution().thirdMax(nums) == 7
