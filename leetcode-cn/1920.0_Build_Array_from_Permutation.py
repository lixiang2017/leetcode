'''
T:O(N),S:O(1)
执行用时：32 ms, 在所有 Python3 提交中击败了97.44% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了11.18% 的用户
'''
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
