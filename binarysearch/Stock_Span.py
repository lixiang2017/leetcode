'''
mono-stack

Success!
Your code took 173 milliseconds — faster than 19.00% in Python
'''
class StockSpan:
    def __init__(self):
        self.d = 0
        self.stack = []

    def next(self, price):
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.d += 1
        days = self.d - (self.stack[-1][1] if self.stack else 0)
        self.stack.append([price, self.d])
        return days
