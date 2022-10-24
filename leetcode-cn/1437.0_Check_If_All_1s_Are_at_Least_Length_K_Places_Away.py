'''
执行用时：76 ms, 在所有 Python3 提交中击败了26.01% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了92.67% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx1 = -1
        for i, x in enumerate(nums):
            if x == 1:
                if idx1 != -1 and i - idx1 - 1 < k:
                    return False
                idx1 = i 
        return True
        