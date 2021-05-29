'''
DP,T:O(N),S:O(1)

执行用时：72 ms, 在所有 Python3 提交中击败了6.13% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了13.83% 的用户
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        jumps = prev_farthest = next_farthest = i = 0
        while i < N:  
            if prev_farthest >= N - 1:
                return jumps

            while i < N and i <= prev_farthest:
                next_farthest = max(next_farthest, i + nums[i])
                i += 1
            jumps += 1
            prev_farthest = next_farthest
