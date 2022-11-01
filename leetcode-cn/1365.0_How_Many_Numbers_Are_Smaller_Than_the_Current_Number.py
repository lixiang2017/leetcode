'''
执行用时：36 ms, 在所有 Python3 提交中击败了91.34% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了88.17% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = sorted(nums)
        return [bisect_left(snums, x) for x in nums]
        