'''
Two Pointers

Runtime: 108 ms, faster than 96.69% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 14.2 MB, less than 51.88% of Python3 online submissions for Sum of Square Numbers.
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c ** 0.5)
        while l <= r:
            t = l * l + r * r
            if t > c:
                r -= 1
            elif t < c:
                l += 1
            else:
                return True
        return False



'''
Fermat Theorem

Runtime: 48 ms, faster than 99.20% of Python3 online submissions for Sum of Square Numbers.
Memory Usage: 14.2 MB, less than 51.88% of Python3 online submissions for Sum of Square Numbers.
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(c ** 0.5)
        for base in range(2, r + 1):
            if c % base:
                continue
            
            exp = 0
            while not(c % base):
                c //= base
                exp += 1
            if base % 4 == 3 and exp % 2 != 0:
                return False
        
        return c % 4 != 3
