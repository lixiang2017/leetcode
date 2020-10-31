'''
use Heron's formula

Success
Details 
Runtime: 288 ms, faster than 25.71% of Python online submissions for Largest Triangle Area.
Memory Usage: 13.2 MB, less than 20.00% of Python online submissions for Largest Triangle Area.
'''


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def euclideanDistance(point1, point2):
            x = point1[0] - point2[0]
            y = point1[1] - point2[1]
            return math.sqrt(x * x + y * y)
        
        def isValidTriangle(a, b, c):
            return a + b > c and a + c > b and b + c > a
        
        max_area = 0
        size = len(points)
        a = b = c = S = 0
        
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    a = euclideanDistance(points[i], points[j])
                    b = euclideanDistance(points[i], points[k])
                    c = euclideanDistance(points[j], points[k])
                    
                    if isValidTriangle(a, b, c):
                        S = (a + b + c) / 2
                        max_area = max(max_area, math.sqrt(S * (S - a) * (S - b) * (S - c)))
        
        return max_area
        

