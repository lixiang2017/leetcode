#! /usr/bin/python
"""
Success
Runtime: 36 ms, faster than 79.42% of Python online submissions for Add Strings.
Memory Usage: 12.1 MB, less than 5.69% of Python online submissions for Add Strings.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from itertools import izip_longest
        carry = 0
        ans = ''
        num1_digit = list(map(int, num1))
        num2_digit = list(map(int, num2))
        for i, j in izip_longest(num1_digit[::-1], num2_digit[::-1], fillvalue=0):
            r = (i + j + carry) % 10
            ans += str(r)
            carry = (i + j + carry) // 10
        if carry:
            ans += '1'
        return ans[::-1]


if __name__ == '__main__':
    num1 = '12'
    num2 = '34'
    assert Solution().addStrings(num1, num2) == '46'

    num1 = '72'
    num2 = '34'
    assert Solution().addStrings(num1, num2) == '106'    