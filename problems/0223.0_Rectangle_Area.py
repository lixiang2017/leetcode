'''
Runtime: 127 ms, faster than 16.03% of Python3 online submissions for Rectangle Area.
Memory Usage: 14 MB, less than 71.27% of Python3 online submissions for Rectangle Area.
'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        overlap = max(0, max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1)))
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        return area_a + area_b - overlap
        