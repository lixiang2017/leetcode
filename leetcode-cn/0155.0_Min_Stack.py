'''
执行用时：60 ms, 在所有 Python3 提交中击败了44.55% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了5.07% 的用户
通过测试用例：31 / 31
'''
class MinStack:

    def __init__(self):
        # (val, minx)
        self.stk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            minx = min(val, self.stk[-1][1])
            self.stk.append((val, minx))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
