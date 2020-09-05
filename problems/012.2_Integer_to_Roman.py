'''
Success
Details 
Runtime: 48 ms, faster than 37.80% of Python online submissions for Integer to Roman.
Memory Usage: 12.8 MB, less than 5.72% of Python online submissions for Integer to Roman.
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return None

        result = []
        digits = []
        numerals = ["I", "V", "X", "L", "C", "D", "M"]
        '''
        while num > 0:
            num, digit = divmod(num, 10)
            digits.append(digit)
        digits.reverse()
        '''
        digits = map(int, map(str, str(num)))

        for i, digit in enumerate(digits):
            index = len(digits) - i - 1
            if digit == 9:
                result.append(numerals[index * 2])
                result.append(numerals[index * 2 + 2])
            elif digit >= 5:
                result.append(numerals[index * 2 + 1])
                result.append(numerals[index * 2] * (digit - 5))
            elif digit == 4:
                result.append(numerals[index * 2])
                result.append(numerals[index * 2 + 1])
            else:
                result.append(numerals[index * 2] * digit)
        return "".join(result)



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
