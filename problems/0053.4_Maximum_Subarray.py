'''
DP

Runtime: 1348 ms, faster than 5.00% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.6 MB, less than 59.05% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            if current_sum <= 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            best_sum = max(best_sum, current_sum)
        return best_sum


'''
Divide Conquer

Runtime: 2500 ms, faster than 5.00% of Python3 online submissions for Maximum Subarray.
Memory Usage: 27.4 MB, less than 99.63% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSub(nums, 0, len(nums) - 1)
    
    def maxSub(self, nums: List[int], left: int, right: int) -> int:
        if left > right:
            return float('-inf')
        mid = (left + right) // 2
        lm = self.maxSub(nums, left, mid - 1)
        rm = self.maxSub(nums, mid + 1, right)
        # best sum from mid-1 to left
        sl = cur = 0
        for i in range(mid - 1, left - 1, -1):
            cur += nums[i]
            sl = max(sl, cur)
        # best sum from mid+1 to right
        sr = cur = 0
        for i in range(mid + 1, right + 1):
            cur += nums[i]
            sr = max(sr, cur)
        
        return max(lm, rm, sl + nums[mid] + sr)
    