'''
Runtime: 42 ms, faster than 72.88% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 95.65% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
    
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n 
        return self.fib(n - 2) + self.fib(n - 1)

'''
Runtime: 45 ms, faster than 66.65% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 95.65% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
    
    def fib(self, n: int) -> int:
        if n <= 1:
            return n 
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b 
        return b
        