'''
You are here!
Your runtime beats 25.86 % of python submissions.
'''

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals = sorted(intervals, cmp = lambda a, b: -1 if a[0] < b[0] or (a[0] == b[0] and a[1] > b[1]) else 1)
        print 'intervals: ', intervals
        
        size = len(intervals)
        res = size
        for i in xrange(size):
            if 0 == i:
                latter = intervals[0][1]
                continue
            if intervals[i][1] <= latter:
                print 'minus one'
                res -= 1
            else:
                latter = intervals[i][1]
        
        return res
                