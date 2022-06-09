'''
执行用时：40 ms, 在所有 Python3 提交中击败了46.69% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了13.97% 的用户
通过测试用例：206 / 206
'''
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if len(points) != 3:
            return False 
        p_set = set()
        for x, y in points:
            p_set.add(x * 100 + y)
        if len(p_set) != 3:
            return False 
        x1, y1 = points[1][0] - points[0][0], points[1][1] - points[0][1]
        x2, y2 = points[2][0] - points[0][0], points[2][1] - points[0][1]
        return x1 * y2 != x2 * y1 
        
        