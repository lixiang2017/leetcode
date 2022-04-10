'''
mod 
hard有时好像也没那么神话。
做这一题的时候，不由自主地联想到另外一个矩形翻转的事情。
边长为x和y的矩形，根据其中一个顶点旋转90度，扩大成另一个矩形。
这一题，还可以根据某条边翻转扩大。 
然后看数据，一直减减减应该不行(更相减损术)，需要取模 -> gcd -> 辗转相除法

执行用时：56 ms, 在所有 Python3 提交中击败了7.14% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了16.96% 的用户
通过测试用例：195 / 195
'''
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        
        while sx < tx and sy < ty:
            if tx < ty:
                ty %= tx 
            else:
                tx %= ty 

        if sx == tx:
            return sy % sx == ty % tx
        elif sy == ty:
            return sx % sy == tx % ty 
        else:
            return False 
