'''

执行用时：60 ms, 在所有 Python3 提交中击败了69.69% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了5.40% 的用户
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        minn = x
        if self.stack:
            minn = min(self.min(), minn)
        self.stack.append([x, minn])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            raise ValueError('Stack is None.')

    def min(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            raise ValueError('Stack is None.')



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
