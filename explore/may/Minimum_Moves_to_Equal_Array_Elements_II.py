'''
approach: to find the median with sort
Time: O(NlogN + N)
Space: O(1)

You are here!
Your runtime beats 49.69 % of python3 submissions.
You are here!
Your memory usage beats 75.16 % of python3 submissions.
'''

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum([abs(num - nums[len(nums) // 2]) for num in nums])


