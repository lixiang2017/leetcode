class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        ans = []
        lefts, rights = 0, s
        for x in nums:
            rights -= x
            ans.append(abs(lefts - rights))
            lefts += x
        return ans


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            nums[i] = abs(left_sum * 2 + x - total)
            left_sum += x
        return nums
