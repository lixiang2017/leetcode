'''
Runtime: 4510 ms, faster than 5.23% of Python3 online submissions for My Calendar III.
Memory Usage: 14.7 MB, less than 56.62% of Python3 online submissions for My Calendar III.
'''
from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = ans = 0
        for delta in self.diff.values():
            cur += delta
            ans = max(ans, cur)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
