'''
binary insert

Runtime: 79 ms, faster than 93.12% of Python3 online submissions for Insert Interval.
Memory Usage: 17.3 MB, less than 91.18% of Python3 online submissions for Insert Interval.
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        ans = []
        for a, b in intervals:
            if not ans or ans[-1][-1] < a:
                ans.append([a, b])
            else:
                ans[-1][-1] = max(ans[-1][-1], b)
        return ans 
        
