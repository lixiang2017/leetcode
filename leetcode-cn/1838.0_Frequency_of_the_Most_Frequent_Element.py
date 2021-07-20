'''
Sort + PreSum + Sliding Window,T:O(NlogN + N + N),S:O(N)
执行用时：700 ms, 在所有 Python3 提交中击败了25.83% 的用户
内存消耗：25.8 MB, 在所有 Python3 提交中击败了8.61% 的用户
'''
from itertools import accumulate
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = list(accumulate(nums))
        most = l = r = 0
        N = len(nums)  
        while r < N:
            while l <= r and l < N and nums[r] * (r - l + 1) - (pre[r] - pre[l] + nums[l]) > k:
                l += 1
            most = max(most, r - l + 1)
            r += 1
        return most


'''
Sort + DP + Sliding Window,T:O(NlogN + N),S:O(N)
执行用时：504 ms, 在所有 Python3 提交中击败了59.97% 的用户
内存消耗：25 MB, 在所有 Python3 提交中击败了27.98% 的用户
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        most = 1  #!!!
        l = total = 0
        N = len(nums)  
        for r in range(1, N):
            total += (r - l) * (nums[r] - nums[r - 1])
            while total > k:
                total -= nums[r] - nums[l]
                l += 1
            most = max(most, r - l + 1)
        return most
