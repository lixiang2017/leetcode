'''
sort

执行用时：204 ms, 在所有 Python3 提交中击败了33.68% 的用户
内存消耗：45.2 MB, 在所有 Python3 提交中击败了45.26% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for p1, p2 in pairwise(points):
            ans = max(ans, p2[0] - p1[0])
        return ans

'''
执行用时：148 ms, 在所有 Python3 提交中击败了69.47% 的用户
内存消耗：45.5 MB, 在所有 Python3 提交中击败了5.27% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(set(x for x, y in points))
        ans = 0
        for x1, x2 in pairwise(xs):
            ans = max(ans, x2 - x1)
        return ans
