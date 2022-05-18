'''
海伦公式
T: O(N^3)
S: O(1)

执行用时：196 ms, 在所有 Python3 提交中击败了34.55% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.33% 的用户
通过测试用例：57 / 57


如果不判断if m < 0, 则会出现
ValueError: math domain error
    return sqrt(p * (p - a) * (p - b) * (p - c))
可能因为三点共线算出来的某一个 p-c 不为0，而是负数。
'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = 0

        def area(pi, pj, pk):
            ix, iy = pi 
            jx, jy = pj 
            kx, ky = pk 
            a = sqrt((ix - jx) * (ix - jx) + (iy - jy) * (iy - jy))
            b = sqrt((ix - kx) * (ix - kx) + (iy - ky) * (iy - ky))
            c = sqrt((jx - kx) * (jx - kx) + (jy - ky) * (jy - ky))
            p = (a + b + c) * 0.5
            m = p * (p - a) * (p - b) * (p - c)
            if m < 0:
                return 0
            return sqrt(m)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    a = area(points[i], points[j], points[k])
                    ans = max(a, ans)
        return ans 

'''
[[35,-23],[-12,-48],[-34,-40],[21,-25],[-35,-44],[24,1],[16,-9],[41,4],[-36,-49],[42,-49],[-37,-20],[-35,11],[-2,-36],[18,21],[18,8],[-24,14],[-23,-11],[-8,44],[-19,-3],[0,-10],[-21,-4],[23,18],[20,11],[-42,24],[6,-19]]
'''


'''
鞋带公式

执行用时：120 ms, 在所有 Python3 提交中击败了83.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了62.73% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(x1, y1, x2, y2, x3, y3):
            return 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)
        
        return max(area(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))


'''
1.向量叉乘
https://blog.csdn.net/qq_36056219/article/details/109057649 
2.利用向量叉积（行列式）求三角形面积
https://blog.csdn.net/aye_hh/article/details/105607088

执行用时：96 ms, 在所有 Python3 提交中击败了90.30% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.03% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def cross(a, b, c, d):
            return a * d - b * c
            
        def area(x1, y1, x2, y2, x3, y3):
            a, b = x2 - x1, y2 - y1 
            c, d = x3 - x1, y3 - y1 
            return 0.5 * abs(cross(a, b, c, d))
        
        return max(area(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))

