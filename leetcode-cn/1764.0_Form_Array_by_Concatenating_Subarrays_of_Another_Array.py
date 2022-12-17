'''
brute force, two pointers

执行用时：40 ms, 在所有 Python3 提交中击败了80.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了98.00% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i, n = 0, len(nums)
        for g in groups:
            m = len(g)
            while i + m <= n and nums[i: i + m] != g:
                i += 1
            if i + m > n:
                return False 
            else:
                i += m
        return True
