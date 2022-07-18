'''
deque

执行用时：68 ms, 在所有 Python3 提交中击败了68.70% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了75.30% 的用户
通过测试用例：11 / 11
'''
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum +=  val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        return self.sum / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
