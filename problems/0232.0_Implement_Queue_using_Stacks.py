'''
Runtime: 63 ms, faster than 18.56% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 14 MB, less than 75.85% of Python3 online submissions for Implement Queue using Stacks.
'''
class MyQueue:

    def __init__(self):
        self.rear = []
        self.front = []

    def push(self, x: int) -> None:
        self.rear.append(x)

    def pop(self) -> int:
        if self.front:
            return self.front.pop()
        else:
            while self.rear:
                self.front.append(self.rear.pop())
            return self.front.pop()

    def peek(self) -> int:
        if self.front:
            return self.front[-1]
        else:
            while self.rear:
                self.front.append(self.rear.pop())
            return self.front[-1]

    def empty(self) -> bool:
        return not self.rear and not self.front


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


'''
Runtime: 65 ms, faster than 12.89% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 14.1 MB, less than 24.36% of Python3 online submissions for Implement Queue using Stacks.
'''
class MyQueue:

    def __init__(self):
        self.rear = []
        self.front = []

    def push(self, x: int) -> None:
        self.rear.append(x)

    def pop(self) -> int:
        self.peek()
        return self.front.pop()

    def peek(self) -> int:
        if not self.front:
            while self.rear:
                self.front.append(self.rear.pop())
        return self.front[-1]

    def empty(self) -> bool:
        return not self.rear and not self.front


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

