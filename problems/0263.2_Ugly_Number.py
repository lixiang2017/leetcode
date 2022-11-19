'''
Runtime: 41 ms, faster than 83.56% of Python3 online submissions for Ugly Number.
Memory Usage: 14 MB, less than 12.22% of Python3 online submissions for Ugly Number.
'''
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for f in [2, 3, 5]:
            while n % f == 0:
                n //= f
        return n == 1
        