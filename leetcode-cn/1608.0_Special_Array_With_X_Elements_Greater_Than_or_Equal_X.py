'''
执行用时：36 ms, 在所有 Python3 提交中击败了77.10% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了18.56% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(0, len(nums) + 1):
            idx = bisect_left(nums, x)
            if len(nums) - idx == x:
                return x 
        return -1
        