'''
Runtime: 161 ms, faster than 85.62% of Python3 online submissions for Data Stream as Disjoint Intervals.
Memory Usage: 18.9 MB, less than 75.92% of Python3 online submissions for Data Stream as Disjoint Intervals.
'''
class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        idx = bisect_right(self.intervals, new_interval)
        merged = False
        # merged with previous one
        if idx > 0 and self.intervals[idx - 1][-1] + 1 >= value:
            merged = True
            self.intervals[idx - 1][-1] = max(self.intervals[idx - 1][-1], value)
        # merged with later one
        if idx < len(self.intervals) and value + 1 >= self.intervals[idx][0]:
            merged = True
            self.intervals[idx][0] = min(self.intervals[idx][0], value)
        # maybe, merged previous one with later one
        if 0 < idx < len(self.intervals) and self.intervals[idx - 1][-1] + 1 >= self.intervals[idx][0]:
            a, b = self.intervals[idx - 1][0], self.intervals[idx][1]
            self.intervals[idx - 1: idx + 1] = [[a, b]]
        # not merged  
        if not merged:
            bisect.insort(self.intervals, new_interval)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
