'''
DP,T:O(N),S:O(1)

执行用时：100 ms, 在所有 Python3 提交中击败了7.83% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了98.01% 的用户
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        farthest = 0

        for i, num in enumerate(nums):
            if farthest >= i:
                farthest = max(farthest, i + num)
            else:
                return False

            if farthest >= N - 1:
                return True
