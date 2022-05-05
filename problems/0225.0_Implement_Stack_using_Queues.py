'''
Runtime: 34 ms, faster than 73.15% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.9 MB, less than 98.98% of Python3 online submissions for Implement Stack using Queues.
'''
'''
q1: sadfak
q2: weruwiowklzdjfalks
'''

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q1) == 0:
            self.q1, self.q2 = self.q2, self.q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        return self.q1.popleft()

    def top(self) -> int:
        if len(self.q1) == 0:
            self.q1, self.q2 = self.q2, self.q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
