'''
pre_max, nums[i - 1], nums[i]
T: O(N)
S: O(1)

执行用时：152 ms, 在所有 Python3 提交中击败了25.00% 的用户
内存消耗：25.2 MB, 在所有 Python3 提交中击败了62.07% 的用户
通过测试用例：226 / 226
'''
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        pre_max = nums[0]
        for i in range(2, n):
            if pre_max > nums[i]:
                return False
            pre_max = max(pre_max, nums[i - 1])
        return True
