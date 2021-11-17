'''
执行用时：92 ms, 在所有 Python3 提交中击败了67.16% 的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了36.57% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        points = Counter()
        all_area = distinct_area = 0
        for x, y, a, b in rectangles:
            points[(x, y)] += 1
            points[(a, b)] += 1
            points[(x, b)] += 1
            points[(a, y)] += 1
            all_area += (a - x) * (b - y)
        
        single = []
        for p, c in points.items():
            if c == 2 or c == 4:
                continue
            elif c == 1:
                single.append(p)
            else:
                return False

        if 4 != len(single):
            return False
        xs = list(set(x for x, y in single))
        ys = list(set(y for x, y in single))
        distinct_area = abs(xs[0] - xs[1]) * abs(ys[0] - ys[1])
        return all_area == distinct_area


'''
只是有四个单点是不行的的（未考虑面积）
[[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]]

[[0,0,4,1],[0,0,4,1]]
'''
