"""
Author: lixiang
Beats: 2.60% -> 3.53% -> 6.18%( # stk = []) -> 0.98%(use pop()) -> 1.87%
"""


class MinStack:

    # stk = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)

    def pop(self):
        """
        :rtype: void
        """
        """
        if self.stk:
            del self.stk[-1]
        """
        self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stk:
            return self.stk[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stk:
            return min(self.stk[:])

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    x = 155
    obj = MinStack()
    obj.push(x)
    obj.pop()
    y = 2233
    z = 1122
    obj.push(y)
    obj.push(z)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)