'''
Runtime: 52 ms, faster than 86.10% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 15.7 MB, less than 6.40% of Python3 online submissions for Maximum Product Subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp, min_dp, ans = [nums[0]], [nums[0]], nums[0]
        n = len(nums)
        for i in range(1, n):
            maxi = max(nums[i], nums[i] * max_dp[-1], nums[i] * min_dp[-1])
            mini = min(nums[i], nums[i] * max_dp[-1], nums[i] * min_dp[-1])
            max_dp.append(maxi)
            min_dp.append(mini)
            ans = max(ans, maxi)
        return ans

'''
Runtime: 56 ms, faster than 68.46% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 14.4 MB, less than 63.75% of Python3 online submissions for Maximum Product Subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxf = minf = ans = nums[0]
        for i in range(1, len(nums)):
            mx, mn = maxf, minf
            maxf = max(nums[i], nums[i] * mx, nums[i] * mn)
            minf = min(nums[i], nums[i] * mx, nums[i] * mn)
            ans = max(ans, maxf)
        return ans
             