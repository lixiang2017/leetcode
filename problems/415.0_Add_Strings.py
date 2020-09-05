#! /usr/bin/python
"""
Success
Runtime: 24 ms, faster than 97.45% of Python online submissions for Add Strings.
Memory Usage: 12 MB, less than 5.69% of Python online submissions for Add Strings.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))


if __name__ == '__main__':
    num1 = '12'
    num2 = '34'
    assert Solution().addStrings(num1, num2) == '46'