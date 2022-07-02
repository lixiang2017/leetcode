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


'''
pairwise

Runtime: 588 ms, faster than 18.06% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
Memory Usage: 28.3 MB, less than 31.88% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        hs = horizontalCuts + [0, h]
        vs = verticalCuts + [0, w]
        hs.sort()
        vs.sort()
        max_h = max(p[1] - p[0] for p in pairwise(hs)) % MOD 
        max_w = max(p[1] - p[0] for p in pairwise(vs)) % MOD 
        return max_h * max_w % MOD 
    
    
'''
Runtime: 689 ms, faster than 5.93% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
Memory Usage: 28.5 MB, less than 28.07% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        MOD = 10 ** 9 + 7
        hs = [0] + horizontalCuts + [h]
        vs = [0] + verticalCuts + [w]
        max_h = max(p[1] - p[0] for p in pairwise(hs)) % MOD 
        max_w = max(p[1] - p[0] for p in pairwise(vs)) % MOD 
        return max_h * max_w % MOD 
    
        
