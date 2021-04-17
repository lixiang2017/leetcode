'''
approach: Map
Time: O(N)
Space: O(N)

Runtime: 60 ms, faster than 77.52% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 14.5 MB, less than 6.56% of Python3 online submissions for Sign of the Product of an Array.
'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        negative = sum(-1 for num in nums if num < 0)
        return -1 if negative % 2 else 1
        