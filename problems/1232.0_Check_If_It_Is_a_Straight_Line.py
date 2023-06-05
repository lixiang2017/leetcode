'''
Runtime: 77 ms, faster than 36.53% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 16.9 MB, less than 27.29% of Python3 online submissions for Check If It Is a Straight Line.
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx, dy = x0 - x1, y0 - y1
        return all(dx * (coordinates[i][1] - y0) == (coordinates[i][0] - x0) * dy for i in range(1, n))
        