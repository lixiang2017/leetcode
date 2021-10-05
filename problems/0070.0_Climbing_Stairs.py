'''
DP

Runtime: 20 ms, faster than 99.01% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.3 MB, less than 11.04% of Python3 online submissions for Climbing Stairs.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b
        return b
