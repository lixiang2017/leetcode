'''
math
T: O(1)
S: O(1)

执行用时：60 ms, 在所有 Python3 提交中击败了16.63% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了33.26% 的用户
通过测试用例：3080 / 3080
'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def intersection(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
            if ax2 <= bx1 or bx2 <= ax1 or by2 <= ay1 or ay2 <= by1:
                return 0
            y = min(ay2, by2) - max(ay1, by1)
            x = min(ax2, bx2) - max(ax1, bx1)
            return x * y
        
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        inter = intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return area_a + area_b - inter


'''
x 或 y 可能 < 0

执行用时：52 ms, 在所有 Python3 提交中击败了40.39% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.68% 的用户
通过测试用例：3080 / 3080
'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def intersection(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
            y = min(ay2, by2) - max(ay1, by1)
            x = min(ax2, bx2) - max(ax1, bx1)
            if x <= 0:
                return 0
            return max(x * y, 0)
        
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        inter = intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return area_a + area_b - inter
