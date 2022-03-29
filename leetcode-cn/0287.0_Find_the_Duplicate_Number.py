'''
T: O(N)
S: O(N)

Runtime: 671 ms, faster than 85.29% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 30.3 MB, less than 22.19% of Python3 online submissions for Find the Duplicate Number.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
