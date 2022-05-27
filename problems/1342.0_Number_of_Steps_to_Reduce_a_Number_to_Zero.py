'''
Runtime: 66 ms, faster than 5.65% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.8 MB, less than 96.14% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if 0 == num:
            return 0
        b = bin(num)
        return (b.count('1') - 1) + len(b) - 2

'''
Runtime: 48 ms, faster than 34.59% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 14 MB, less than 8.69% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = bin(num)
        return (b.count('1') - 1) + len(b) - 2


'''
simulation

Runtime: 65 ms, faster than 6.33% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.8 MB, less than 53.50% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            step += 1
        return step

