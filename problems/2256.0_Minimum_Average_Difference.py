'''
prefix sum
T: O(N)
S: O(1)

Runtime: 973 ms, faster than 98.05% of Python3 online submissions for Minimum Average Difference.
Memory Usage: 24.8 MB, less than 80.12% of Python3 online submissions for Minimum Average Difference.
'''
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, total = len(nums), sum(nums)
        s = 0
        min_diff = total // n
        ans = n - 1
        for i in range(n - 1):
            s += nums[i]
            diff = abs(s // (i + 1) - (total - s) // (n - i - 1))
            if diff < min_diff or (diff == min_diff and i < ans):
                ans = i 
                min_diff = diff
        return ans 
