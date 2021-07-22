'''
approach: PreMax + PostMin
Time: O(2N)
Space: O(N)

You are here!
Your runtime beats 76.97 % of python3 submissions.
You are here!
Your memory usage beats 68.12 % of python3 submissions.
'''
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        premax, postmin = nums[0], [nums[-1]] * N
        for i in range(N - 2, -1, -1):
            postmin[i] = min(nums[i], postmin[i + 1])
        
        for i in range(N - 1):
            premax = max(premax, nums[i])
            if premax <= postmin[i + 1]:
                return i + 1

