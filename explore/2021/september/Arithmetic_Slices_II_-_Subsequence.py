'''
DP 
Time: O(N^2)
Space: O(N^2)

You are here!
Your runtime beats 6.22 % of python3 submissions.
You are here!
Your memory usage beats 43.54 % of python3 submissions.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        f = [defaultdict(int) for _ in nums]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                ans += f[j][d]
                f[i][d] += f[j][d] + 1
        return ans
