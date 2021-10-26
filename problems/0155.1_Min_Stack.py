'''
Runtime: 133 ms, faster than 27.16% of Python3 online submissions for Min Stack.
Memory Usage: 18.2 MB, less than 56.21% of Python3 online submissions for Min Stack.
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:  
        if not self.stack:
            self.stack.append(val)
            self.min.append(val)
        else:
            self.stack.append(val)
            self.min.append(min(self.min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



'''
Runtime: 56 ms, faster than 92.19% of Python3 online submissions for Min Stack.
Memory Usage: 18.5 MB, less than 19.41% of Python3 online submissions for Min Stack.
'''
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


