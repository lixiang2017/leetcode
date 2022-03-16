'''
two queues

执行用时：40 ms, 在所有 Python3 提交中击败了28.35% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了78.31% 的用户
通过测试用例：16 / 16
'''
class MyStack:

    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        # O(N)
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


'''
one queue

执行用时：24 ms, 在所有 Python3 提交中击败了98.33% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了36.68% 的用户
通过测试用例：16 / 16
'''
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # O(N)
        n = len(self.q)
        self.q.append(x)
        for _ in range(n):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



'''
list

执行用时：44 ms, 在所有 Python3 提交中击败了10.04% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了92.00% 的用户
通过测试用例：16 / 16
'''
class MyStack:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return not self.s 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


'''
one deque

执行用时：36 ms, 在所有 Python3 提交中击败了55.94% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了96.10% 的用户
通过测试用例：16 / 16
'''
class MyStack:

    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        return self.d.pop()

    def top(self) -> int:
        return self.d[-1]

    def empty(self) -> bool:
        return not self.d


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



