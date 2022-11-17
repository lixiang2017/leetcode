'''
Runtime: 46 ms, faster than 73.40% of Python3 online submissions for Rectangle Overlap.
Memory Usage: 13.9 MB, less than 67.85% of Python3 online submissions for Rectangle Overlap.
'''
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        overlap = max(0, max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1)))
        return overlap > 0
        