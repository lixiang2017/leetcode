'''
Success
Details 
Runtime: 44 ms, faster than 50.49% of Python online submissions for Integer to Roman.
Memory Usage: 12.6 MB, less than 5.72% of Python online submissions for Integer to Roman.
'''

symbol2value = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

value2symbol = {v: k for k, v in symbol2value.iteritems()}

roman_inc = {
    1: 'I',
    4: 'IV', 
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}

roman_desc = sorted(roman_inc.iteritems(), key=lambda d:d[0], reverse=True)


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return None

        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = '', 0
        while num:
            res += (num // values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res


if __name__ == '__main__':
    num = 3
    output = "III"
    assert (Solution().intToRoman(num) == output)

    num = 4
    output = "IV"
    assert (Solution().intToRoman(num) == output)

    num = 9
    output = "IX"
    assert (Solution().intToRoman(num) == output)

    num = 58
    output = "LVIII"
    # Explanation: L = 50, V = 5, III = 3.
    assert (Solution().intToRoman(num) == output)

    num = 1994
    output = "MCMXCIV"
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    assert (Solution().intToRoman(num) == output)
