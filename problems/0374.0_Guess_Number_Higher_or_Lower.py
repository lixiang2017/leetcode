'''
Runtime: 44 ms, faster than 21.48% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14 MB, less than 89.41% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)
            if 0 == g:
                return mid
            elif 1 == g:
                l = mid + 1
            else:
                r = mid - 1


'''
DFS

Runtime: 45 ms, faster than 20.46% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.3 MB, less than 10.10% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.guess_rec(1, n)

    def guess_rec(self, l: int, r: int) -> int:
        mid = (l + r) // 2
        g = guess(mid)
        if 0 == g:
            return mid
        elif 1 == g:
            return self.guess_rec(mid + 1, r)
        else:
            return self.guess_rec(l, mid - 1)


'''
Runtime: 69 ms, faster than 5.52% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.3 MB, less than 42.17% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        class C:
            def __getitem__(self, i):
                return -guess(i)
            
        return bisect.bisect_left(C(), 0, 1, n)


'''
lambda _, i 中的 _ 是不是相当于省略的 self ？

Runtime: 50 ms, faster than 13.06% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.3 MB, less than 10.10% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect_left(C(), 0, 1, n)


'''
Runtime: 62 ms, faster than 5.52% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.2 MB, less than 42.17% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect_right(C(), -1, 1, n)


'''
Runtime: 50 ms, faster than 13.06% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.2 MB, less than 71.96% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        class C: __getitem__ = lambda self, i: -guess(i)
        return bisect_right(C(), -1, 1, n)


'''
Runtime: 24 ms, faster than 95.09% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.3 MB, less than 42.17% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        class C: __getitem__ = lambda something_useless, i: -guess(i)
        return bisect_right(C(), -1, 1, n)


'''
Ternary Search

Runtime: 32 ms, faster than 62.57% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 14.3 MB, less than 42.17% of Python3 online submissions for Guess Number Higher or Lower.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid1 = l + (r - l) // 3
            mid2 = r - (r - l) // 3
            g1, g2 = guess(mid1), guess(mid2)
            if 0 == g1:
                return mid1
            elif 0 == g2:
                return mid2
            elif g1 < 0:
                r = mid1 - 1
            elif g2 > 0:
                l = mid2 + 1
            else:
                l, r = mid1 + 1, mid2 - 1
                







