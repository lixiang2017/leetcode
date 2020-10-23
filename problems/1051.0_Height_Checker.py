'''
Success
Details
Runtime: 24 ms, faster than 65.30% of Python online submissions for Height Checker.
Memory Usage: 13.6 MB, less than 9.79% of Python online submissions for Height Checker.
'''

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        moves = 0
        new_heights = sorted(heights)
        for i, j in zip(heights, new_heights):
            if i != j:
                moves += 1
        return moves
    