'''
Runtime: 166 ms, faster than 30.13% of Python3 online submissions for Remove Covered Intervals.
Memory Usage: 14.4 MB, less than 86.23% of Python3 online submissions for Remove Covered Intervals.
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda inter: (inter[0], -inter[1]))
        ans, last = [intervals[0]], intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            a, b = intervals[i]
            if b <= last:
                continue
            else:
                last = b
                ans.append([a, b])
        
        return len(ans)


'''
Runtime: 131 ms, faster than 53.51% of Python3 online submissions for Remove Covered Intervals.
Memory Usage: 14.5 MB, less than 74.29% of Python3 online submissions for Remove Covered Intervals.
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda inter: (inter[0], -inter[1]))
        ans, last = 1, intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            a, b = intervals[i]
            if b <= last:
                continue
            else:
                last = b
                ans += 1
        
        return ans
    
