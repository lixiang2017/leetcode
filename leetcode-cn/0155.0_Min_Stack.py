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


'''
执行用时：56 ms, 在所有 Python3 提交中击败了82.80% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了5.13% 的用户
通过测试用例：31 / 31
'''
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            minx = min(val, self.stack[-1][-1])
            self.stack.append([val, minx])

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

