'''
xorsum, T: O(2N), S: O(1)

执行用时：72 ms, 在所有 Python3 提交中击败了44.84% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了84.31% 的用户
通过测试用例：44 / 44
'''
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        xorsum = 0
        for x in chain(nums, range(1, n + 1)):
            xorsum ^= x 
        # xorsum = x1 ^ x2 
        lsb = xorsum & -xorsum 
        type1 = type2 = 0 
        for x in chain(nums, range(1, n + 1)):
            if x & lsb:
                type1 ^= x 
            else:
                type2 ^= x
        return [type1, type2]
