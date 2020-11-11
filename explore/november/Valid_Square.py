'''
You are here!
Your runtime beats 55.91 % of python submissions.
'''


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 == p3 == p4:  # !!!
            return False
        
        from itertools import combinations
        
        points = [p1, p2, p3, p4]
        edges = []  # 6 edges
        # two_points = 
        for point1, point2 in combinations(points, 2):
            length = self.lengthBetweenPoints(point1, point2)
            edges.append(length)
        
        edges.sort()
        return True if edges[0] == edges[1] == edges[2] == edges[3] and edges[4] == edges[5] else False
    
    from math import sqrt
    def lengthBetweenPoints(self, point1, point2):
        x_diff = point1[0] - point2[0]
        y_diff = point1[1] - point2[1]
        return sqrt(x_diff ** 2 + y_diff ** 2)
    
    
'''
Submission Result: Wrong Answer 
Input: [0,0]
[0,0]
[0,0]
[0,0]
Output: true
Expected: false
'''
    