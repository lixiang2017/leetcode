'''
Approach #1: Brute Force [Aceepted]
use Shoelace formula/Algorithm

Success
Details 
Runtime: 108 ms, faster than 82.86% of Python online submissions for Largest Triangle Area.
Memory Usage: 13.3 MB, less than 20.00% of Python online submissions for Largest Triangle Area.
'''

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p, q, r):
            return .5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1] -
                           p[1] * q[0] - q[1] * r[0] - r[1] * p[0])
    
        return max(area(*triangle) for triangle in itertools.combinations(points, 3))
        