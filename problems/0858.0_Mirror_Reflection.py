'''
Runtime: 67 ms, faster than 9.90% of Python3 online submissions for Mirror Reflection.
Memory Usage: 14 MB, less than 16.83% of Python3 online submissions for Mirror Reflection.
'''
'''
画图画图，把镜像再翻折展开成更大的面积
p/q:
0   3/2 5/2 7/2 9/2 11/2 ... 7/4 9/4 11/4 ...
1   1/1 3/1 5/1 ... 5/3 7/3 ..
2   2/1 4/1 6/1 ... 4/3 6/3 8/3 10/3 ...
'''

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p //= g 
        q //= g 
        if p & 1 and q & 1:
            return 1 
        elif p & 1 == 0 and q & 1:
            return 2
        else:
            return 0
            