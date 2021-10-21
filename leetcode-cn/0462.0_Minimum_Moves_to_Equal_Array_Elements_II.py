'''
sort + median

执行用时：44 ms, 在所有 Python3 提交中击败了27.69% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了23.08% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        return sum([abs(x - nums[N // 2]) for x in nums])
