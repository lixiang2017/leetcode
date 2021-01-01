'''
You are here!
Your runtime beats 90.52 % of python submissions.
'''


class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda interval: (interval[0], -interval[1]))
        
        res = [intervals[0]]
        for i, j in intervals[1:]:
            if j > res[-1][1]:
                res.append([i, j])
        
        return len(res)
            