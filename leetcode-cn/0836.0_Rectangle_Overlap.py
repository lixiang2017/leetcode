'''
Math
T: O(1)
O: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了34.04% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了95.18% 的用户
通过测试用例：40 / 40
'''
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        if min(ax2, bx2) <= max(ax1, bx1) or min(ay2, by2) <= max(ay1, by1):
            return False
        else:
            return True
