'''
monotonic stack
T: O(N)
S: O(N)

执行用时：336 ms, 在所有 Python3 提交中击败了50.51% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了70.99% 的用户
通过测试用例：99 / 99
'''
class StockSpanner:

    def __init__(self):
        self.idx = -1
        # desc stack
        self.stack = []

    def next(self, price: int) -> int:
        self.idx += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        span = self.idx - self.stack[-1][1] if self.stack else self.idx + 1
        self.stack.append((price, self.idx))
        return span 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


'''
Runtime: 1150 ms, faster than 16.97% of Python3 online submissions for Online Stock Span.
Memory Usage: 19.6 MB, less than 39.40% of Python3 online submissions for Online Stock Span.
'''
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.i += 1
        ans = self.i - (self.stack[-1][1] if self.stack else 0)
        self.stack.append([price, self.i])
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


