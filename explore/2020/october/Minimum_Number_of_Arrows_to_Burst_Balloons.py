'''
You are here!
Your runtime beats 80.40 % of python submissions.
'''


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        size = len(points)
        if size < 2:
            return size
        
        # sort by start of point
        points.sort(key = lambda point: point[0])
        
        res = 1
        end = points[0][1]
        
        for i in xrange(1, size):
            if points[i][0] > end:
                res += 1
                end = points[i][1]
            else:
                end = min(end, points[i][1])
        return res