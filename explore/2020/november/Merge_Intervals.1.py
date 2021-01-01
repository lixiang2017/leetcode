'''
You are here!
Your runtime beats 98.59 % of python submissions.
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
        # merged = [intervals[0]]
        # size = len(intervals)
        # for i in range(1, size):
        merged = []
        for interval in intervals:
            # start, end = interval
            # last_start, last_end = merged[-1]
            
            # if the list of merged intervals is empty or if the current 
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and the previous interval.
                merged[-1][1] = max(interval[1], merged[-1][1])
        
        return merged