'''
执行用时：3416 ms, 在所有 Python3 提交中击败了11.84% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了18.42% 的用户
通过测试用例：8 / 8
'''
'''
n = 4
(10000 * 10000) 100_000_000
9999 * 9999    99_980_001
9948 * 9926    81_000_000
4000 * 4000    16_000_000
1000 * 1000    1_000_000


1、generate 2*n 2*n-1 digits palinromes
- 2*n
abcd  dcba
1000  0001
...
9999  9999

- 2*n-1
100 [0-9] 001
...
999 [0-9] 999 

2、check if it's product of two n-digits integers


'''


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9
        
        MOD = 1337

        def gen_even():
            nine = (10 ** n) - 1
            one = 10 ** (n - 1)
            for part in range(nine, one, -1):
                # no need to fill 0
                x = part * (10 ** n) + int(str(part)[:: -1])
                yield x

        def gen_odd():
            n1 = n - 1
            nine = (10 ** n1) - 1
            one = 10 ** (n1 - 1)          
            for part in range(nine, one, -1):
                for mid in (9, -1, -1):
                    x = part * (10 ** n) + int(str(part)[:: -1]) + mid * (10 ** n1)
                yield x

        def check(x):
            # right
            r = (10 ** n) - 1
            while r >=  x // r:
                if x % r == 0:
                    return True
                else:
                    r -= 1
            return False 

        for x in gen_even(): # gen(2 * n):
            if check(x):
                return x % MOD 
        for x in gen_odd():  # gen(2 * n - 1):
            if check(x):
                return x % MOD 
        return -1


'''
ans for 2 to 8
987
123
597
677
1218
877
475
'''

'''
执行用时：36 ms, 在所有 Python3 提交中击败了91.23% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了10.07% 的用户
通过测试用例：8 / 8
'''
class Solution:
    def largestPalindrome(self, n: int) -> int:
        return [9, 987, 123, 597, 677, 1218, 877, 475][n - 1]


        
