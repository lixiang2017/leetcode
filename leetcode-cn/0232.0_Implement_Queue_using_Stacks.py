'''
执行用时：20 ms, 在所有 Python 提交中击败了48.16%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了93.77%的用户
'''



class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


'''
two stacks

执行用时：40 ms, 在所有 Python3 提交中击败了27.51% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了21.95% 的用户
通过测试用例：22 / 22
'''
class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        # move elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


'''
in_stack -> out_stack

执行用时：28 ms, 在所有 Python3 提交中击败了93.60% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了90.29% 的用户
通过测试用例：22 / 22
'''
class MyQueue:

    def __init__(self):
        self.in_s, self.out_s = [], []

    def push(self, x: int) -> None:
        self.in_s.append(x)

    def pop(self) -> int:
        if self.out_s:
            return self.out_s.pop()
        else:
            while self.in_s:
                self.out_s.append(self.in_s.pop())
            return self.out_s.pop()

    def peek(self) -> int:
        if self.out_s:
            return self.out_s[-1]
        else:
            while self.in_s:
                self.out_s.append(self.in_s.pop())
            return self.out_s[-1]
            
    def empty(self) -> bool:
        return not self.in_s and not self.out_s


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


'''
in_stack -> out_stack, simple

执行用时：28 ms, 在所有 Python3 提交中击败了93.60% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.28% 的用户
通过测试用例：22 / 22
'''
class MyQueue:

    def __init__(self):
        self.in_s, self.out_s = [], []

    def push(self, x: int) -> None:
        self.in_s.append(x)

    def in2out(self) -> None:
        while self.in_s:
            self.out_s.append(self.in_s.pop())

    def pop(self) -> int:
        if not self.out_s:
            self.in2out()
        return self.out_s.pop()

    def peek(self) -> int:
        if not self.out_s:
            self.in2out()
        return self.out_s[-1]

    def empty(self) -> bool:
        return not self.in_s and not self.out_s


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()




