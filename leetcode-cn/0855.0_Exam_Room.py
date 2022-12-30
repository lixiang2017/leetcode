'''
执行用时：3988 ms, 在所有 Python3 提交中击败了71.21% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了28.79% 的用户
通过测试用例：126 / 126
'''
from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, n: int):
        self.sl = SortedList()
        self.n = n

    def seat(self) -> int:
        if not self.sl:
            self.sl.add(0)
            return 0
        
        diff, idx = self.sl[0], 0
        for x, y in pairwise(self.sl):
            if (y - x) // 2 > diff:
                diff = (y - x) // 2
                idx = x + (y - x) // 2
        
        if self.n - 1 - self.sl[-1] > diff:
            idx = self.n - 1
        self.sl.add(idx)
        return idx 

    def leave(self, p: int) -> None:
        self.sl.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)


'''
执行用时：3952 ms, 在所有 Python3 提交中击败了71.21% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了59.85% 的用户
通过测试用例：126 / 126
'''
class ExamRoom:

    def __init__(self, n: int):
        self.n = n 
        self.s = []

    def seat(self) -> int:
        if not self.s:
            self.s.append(0)
            return 0
        if 1 == len(self.s):
            if self.s[0] - 0 >= self.n - 1 - self.s[0]:
                self.s = [0] + self.s 
                return 0
            else:
                self.s.append(self.n - 1)
                return self.n - 1
        max_d = self.s[0]
        p = 0
        for a, b in pairwise(self.s):
            if (b - a) // 2 > max_d:
                max_d = (b - a) // 2
                p = a + (b - a) // 2
        if self.n - 1 - self.s[-1] > max_d:
            p = self.n - 1
        bisect.insort(self.s, p)
        return p 

    def leave(self, p: int) -> None:
        i = bisect_left(self.s, p)
        self.s.pop(i)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

