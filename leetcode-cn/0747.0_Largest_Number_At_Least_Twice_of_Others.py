'''
T: O(2N), S:O(1)

执行用时：24 ms, 在所有 Python3 提交中击败了98.35% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.66% 的用户
通过测试用例：232 / 232
'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxv = max(nums)
        maxv_idx = 0
        for i, x in enumerate(nums):
            if x == maxv:
                maxv_idx = i 
            elif x * 2 > maxv:
                return -1
        return maxv_idx
