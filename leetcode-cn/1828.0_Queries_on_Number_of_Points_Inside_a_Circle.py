'''
brute force

执行用时：628 ms, 在所有 Python3 提交中击败了93.95% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了55.81% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        m = len(queries)
        ans = [0] * m
        for i, (x, y, r) in enumerate(queries):
            for x1, y1 in points:
                if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
                    ans[i] += 1
        return ans 

'''
sort + binary search

执行用时：552 ms, 在所有 Python3 提交中击败了98.14% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了95.35% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(points)
        points.sort()
        m = len(queries)
        ans = [0] * m
        for i, (x, y, r) in enumerate(queries):
            idx = bisect_left(points, [x - r, -1])
            for j in range(idx, n):
                x1, y1 = points[j]
                if x + r < x1:
                    break
                if (x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r:
                    ans[i] += 1
        return ans 
