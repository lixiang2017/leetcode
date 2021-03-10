'''
Time: O(13 * 3) = O(1)
Space: O(1)

You are here!
Your runtime beats 87.82 % of python submissions.
You are here!
Your memory usage beats 71.88 % of python submissions.
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ValueSymbol = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        roman = ''
        for value, symbol in ValueSymbol:
            while num >= value:
                roman += symbol
                num -= value
        return roman        
