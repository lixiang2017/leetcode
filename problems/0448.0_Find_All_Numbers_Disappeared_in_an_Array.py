'''
ref:
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation

Runtime: 372 ms, faster than 55.30% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22.2 MB, less than 60.62% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])
        return [i + 1 for i, x in enumerate(nums) if x > 0]
