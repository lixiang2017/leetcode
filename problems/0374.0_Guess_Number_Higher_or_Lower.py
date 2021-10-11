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
