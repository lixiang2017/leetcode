'''
binary search

Runtime: 251 ms, faster than 93.52% of Python3 online submissions for My Calendar I.
Memory Usage: 14.7 MB, less than 92.29% of Python3 online submissions for My Calendar I.
'''
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.append([start, end])
            return True 
        idx = bisect_left(self.calendar, [start, end])
        if (idx >= 1 and self.calendar[idx - 1][1] > start) or \
                (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False 
        bisect.insort(self.calendar, [start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


'''
Runtime: 318 ms, faster than 78.43% of Python3 online submissions for My Calendar I.
Memory Usage: 14.8 MB, less than 58.88% of Python3 online submissions for My Calendar I.
'''
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self.calendar, [start, end])
        if (idx >= 1 and self.calendar[idx - 1][1] > start) or \
                (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False 
        bisect.insort(self.calendar, [start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
