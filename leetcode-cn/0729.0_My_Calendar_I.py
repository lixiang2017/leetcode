'''
binary search
[[start, end]], not [start, end]

执行用时：152 ms, 在所有 Python3 提交中击败了97.73% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了73.61% 的用户
通过测试用例：107 / 107
'''
class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if not self.intervals:
            self.intervals.append([start, end])
            return True 

        idx = bisect_right(self.intervals, [start, end])
        if idx == len(self.intervals):
            if self.intervals[-1][-1] > start:
                return False
            else:
                self.intervals.append([start, end])
                return True 
        elif idx == 0:
            if end > self.intervals[0][0]:
                return False 
            else:
                self.intervals[0: 0] = [[start, end]]
                return True 
        else:
            if self.intervals[idx-1][1] > start or end > self.intervals[idx][0]:
                return False 
            if self.intervals[idx-1][1] == start and self.intervals[idx][0] == end:
                self.intervals[idx - 1 : idx + 1] = [[self.intervals[idx-1][0], self.intervals[idx][1]]]
                return True 
            elif self.intervals[idx-1][1] == start:
                self.intervals[idx - 1][1] = end 
                return True 
            elif self.intervals[idx][0] == end:
                self.intervals[idx][0] = start 
                return True 
            else:
                self.intervals[idx: idx] = [[start, end]]
                return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


