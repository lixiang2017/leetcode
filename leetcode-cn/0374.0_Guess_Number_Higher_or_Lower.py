'''
binary search

执行用时：40 ms, 在所有 Python3 提交中击败了25.63% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了27.52% 的用户
通过测试用例：25 / 25
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, (1 << 31) - 1
        while l <= h:
            mid = l + (h - l) // 2
            g = guess(mid)
            if 0 == g:
                return mid 
            elif -1 == g:
                h = mid - 1
            else:
                l = mid + 1
        return l 

