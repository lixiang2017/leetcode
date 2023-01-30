'''
Runtime: 38 ms, faster than 41.59% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 13.8 MB, less than 54.01% of Python3 online submissions for N-th Tribonacci Number.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        for _ in range(n - 2):
            t[0], t[1], t[2] = t[1], t[2], t[0] + t[1] + t[2]
        return t[-1]
            
'''
Runtime: 27 ms, faster than 90.72% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 13.8 MB, less than 54.01% of Python3 online submissions for N-th Tribonacci Number.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        a, b, c = t
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
            