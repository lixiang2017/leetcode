'''
Runtime: 36 ms, faster than 41.67% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
Memory Usage: 14.3 MB, less than 19.23% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
'''
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(1 for p in position if p & 1)
        even = len(position) - odd
        return min(odd, even)
        