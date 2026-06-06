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
