'''
You are here!
Your runtime beats 99.21 % of python3 submissions.
You are here!
Your memory usage beats 40.88 % of python3 submissions.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = {}
        for i, n in enumerate(nums):
            if target - n in num2idx:
                return [num2idx[target - n], i]
            num2idx[n] = i

