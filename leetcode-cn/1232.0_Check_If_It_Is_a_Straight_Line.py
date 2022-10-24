'''
执行用时：68 ms, 在所有 Python3 提交中击败了59.97% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了65.53% 的用户
通过测试用例：79 / 79
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True 
        dx0, dy0 = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        for i in range(2, n):
            dx1, dy1 = coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1]
            if dx1 * dy0 != dx0 * dy1:
                return False 
        return True 
        