'''

You are here!
Your runtime beats 88.11 % of python3 submissions.
You are here!
Your memory usage beats 79.86 % of python3 submissions.
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
        