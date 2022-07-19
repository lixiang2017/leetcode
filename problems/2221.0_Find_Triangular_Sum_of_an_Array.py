'''
T: O(N^2)
S: O(N)

Runtime: 1856 ms, faster than 85.33% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 14 MB, less than 53.78% of Python3 online submissions for Find Triangular Sum of an Array.
'''
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(a + b) % 10 for a, b in pairwise(nums)]
        return nums[0]
