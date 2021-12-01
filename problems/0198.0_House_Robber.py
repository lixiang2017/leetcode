'''
DP
T: O(N)
S: O(1)

Runtime: 32 ms, faster than 70.60% of Python3 online submissions for House Robber.
Memory Usage: 14.3 MB, less than 52.92% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        r = not_r = 0
        for x in nums:
            r, not_r = not_r + x, max(r, not_r)
        return max(r, not_r)
            
