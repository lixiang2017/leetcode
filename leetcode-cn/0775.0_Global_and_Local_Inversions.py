'''
执行用时：128 ms, 在所有 Python3 提交中击败了53.41% 的用户
内存消耗：24.7 MB, 在所有 Python3 提交中击败了88.64% 的用户
通过测试用例：226 / 226
'''
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        pre_max = -1
        for i in range(1, n):
            if pre_max > nums[i]:
                return False 
            pre_max = max(pre_max, nums[i - 1])
        return True
        