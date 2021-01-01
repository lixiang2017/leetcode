'''
You are here!
Your runtime beats 64.84 % of python submissions.
'''



class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        intervals.sort(key = lambda interval: interval[0])
        merged = [intervals[0]]
        size = len(intervals)
        for i in range(1, size):
            start, end = intervals[i]
            last_start, last_end = merged[-1]
            if last_end < start:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(end, last_end)
        
        return merged