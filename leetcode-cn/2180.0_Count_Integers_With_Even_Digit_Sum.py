'''
math
T: O(log num)
S: O(1)

0 1 2 3 4 5 6 7 8 9  10
E O E O E O E O E O  O    (Even or Odd)
every 10 numbers (from 0 to 9) will be a group with 5 even numbers and 5 odd numbers.

99 100
E   O       switch
999 1000
O    O      same as before
9999 10000
E    O      switch

执行用时：28 ms, 在所有 Python3 提交中击败了99.38% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了65.43% 的用户
通过测试用例：71 / 71
'''
class Solution:
    def countEven(self, num: int) -> int:
        if num < 10:
            return num // 2
        a, b = divmod(num, 10)
        ans = (a * 10 // 2) - 1  # need to remove 0
        # t = digit sum of a 
        t = 0
        while a:
            t += a % 10
            a //= 10
        ans += (b + 1) // 2
        if (b + 1) & 1 and t & 1 == 0:
            ans += 1
        return ans 

'''
no need for num < 10

执行用时：28 ms, 在所有 Python3 提交中击败了99.38% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了32.10% 的用户
通过测试用例：71 / 71
'''
class Solution:
    def countEven(self, num: int) -> int:
        a, b = divmod(num, 10)
        ans = (a * 10 // 2) - 1  # need to remove 0
        # t = digit sum of a 
        t = 0
        while a:
            t += a % 10
            a //= 10
        ans += (b + 1) // 2
        if (b + 1) & 1 and t & 1 == 0:
            ans += 1
        return ans 

'''
brute force
T: O(NlogN)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了51.23% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了65.43% 的用户
通过测试用例：71 / 71
'''
class Solution:
    def countEven(self, num: int) -> int:
        def isEven(x: int) -> bool:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s & 1 == 0

        return sum(isEven(x) for x in range(1, num + 1))
