'''
Runtime: 1634 ms, faster than 74.16% of Python3 online submissions for K Radius Subarray Averages.
Memory Usage: 35 MB, less than 33.33% of Python3 online submissions for K Radius Subarray Averages.
'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        total = sum(nums[: 2 * k])
        for i in range(k, n - k):
            if i - k - 1 >= 0:
                total -= nums[i - k - 1]
            if i + k < n:
                total += nums[i + k]
            ans[i] = total // (2 * k + 1)
        return ans 
        