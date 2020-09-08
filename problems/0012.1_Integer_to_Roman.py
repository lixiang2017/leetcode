'''
Success
Details 
Runtime: 44 ms, faster than 50.49% of Python online submissions for Integer to Roman.
Memory Usage: 12.9 MB, less than 5.72% of Python online submissions for Integer to Roman.
'''


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
        res = ''
        for i, v in enumerate(values):
            res += (num // v) * numerals[i]
            num %= v
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
