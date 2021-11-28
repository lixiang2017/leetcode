'''
69 / 69 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 25.6 MB
提交时间：1 天前
'''
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sy, sx = startPos
        hy, hx = homePos
        ans = 0
        if sx < hx:
            ans += sum(colCosts[sx + 1: hx + 1])
        else:
            ans += sum(colCosts[hx: sx])
        
        if sy < hy:
            ans += sum(rowCosts[sy + 1: hy + 1])
        else:
            ans += sum(rowCosts[hy: sy])
            
        return ans

'''
[1,0]
[2,3]
[5,4,3]
[8,2,6,7]
[0,0]
[0,0]
[5]
[26]
[0,0]
[1,2]
[10,2,5]
[10,6,1]
'''

