'''
DP

You are here!
Your runtime beats 99.05 % of python3 submissions
You are here!
Your memory usage beats 69.95 % of python3 submissions.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n < 3:
            return t[n]
        a, b, c = t
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
