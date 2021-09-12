'''
AC
'''
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = defaultdict(int)
        for w, h in rectangles:
            ratio[w/h] += 1
        ans = 0
        for wh, c in ratio.items():
            if c >= 2:
                ans += c * (c - 1) // 2
        return ans
            