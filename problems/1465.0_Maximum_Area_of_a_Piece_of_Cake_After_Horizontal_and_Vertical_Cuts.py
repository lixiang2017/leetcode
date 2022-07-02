'''
sort 

Runtime: 651 ms, faster than 7.62% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
Memory Usage: 28.2 MB, less than 34.98% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        hs = horizontalCuts + [0, h]
        vs = verticalCuts + [0, w]
        hs.sort()
        vs.sort()
        max_h = max(hs[i] - hs[i - 1] for i in range(1, len(hs)))
        max_w = max(vs[i] - vs[i - 1] for i in range(1, len(vs)))
        return max_h * max_w % MOD 
