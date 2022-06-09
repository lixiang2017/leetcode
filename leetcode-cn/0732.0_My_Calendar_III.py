'''
有序字典+差分数组
T: O(N^2)
S: O(N)

执行用时：1436 ms, 在所有 Python3 提交中击败了36.55% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了36.55% 的用户
通过测试用例：98 / 98
'''
from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        if start in self.d:
            self.d[start] += 1
        else:
            self.d[start] = 1
        if end in self.d:
            self.d[end] -= 1
        else:
            self.d[end] = -1

        ans = book = 0
        for freq in self.d.values():
            book += freq 
            ans = max(ans, book)
        return ans 

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)


