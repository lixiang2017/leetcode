'''
执行用时：40 ms, 在所有 Python3 提交中击败了80.23% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了57.03% 的用户
通过测试用例：90 / 90
'''
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_area = sum(z != 0 for xy in grid for z in xy)
        yz_area = sum(max(chain(*xs)) for xs in zip(grid)) 
        xz_area = sum(max(ys) for ys in zip(*grid))
        return xy_area + yz_area + xz_area


        