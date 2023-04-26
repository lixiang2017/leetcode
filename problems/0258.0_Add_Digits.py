'''
Runtime: 50 ms, faster than 34.24% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 91.66% of Python3 online submissions for Add Digits.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            t = 0
            while num:
                t += (num % 10)
                num //= 10
            num = t
        return num

'''
https://en.wikipedia.org/wiki/Digital_root

Runtime: 37 ms, faster than 86.34% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 54.54% of Python3 online submissions for Add Digits.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            x = 0
            while num:
                x += num % 10 
                num //= 10
            num = x 
        return num 


'''
Runtime: 60 ms, faster than 26.47% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 54.54% of Python3 online submissions for Add Digits.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0 
        if num % 9 == 0:
            return 9 
        return num % 9


'''
Runtime: 27 ms, faster than 93.41% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 39.79% of Python3 online submissions for Add Digits.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
        