class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict0 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        dict1 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        ans = 0
        l = len(s)
        i = 0

        while i < l:
            if s[i:i + 2] in dict1.keys():
                ans += dict1[s[i:i + 2]]
                i += 2
            else:
                ans += dict0[s[i]]
                i += 1

        return ans

if __name__ == "__main__":
    s = "III"
    print(Solution().romanToInt(s))
    assert (Solution().romanToInt(s) == 3)

    s = "IV"
    print(Solution().romanToInt(s))
    assert (Solution().romanToInt(s) == 4)

    s = "IX"
    print(Solution().romanToInt(s))
    assert (Solution().romanToInt(s) == 9)

    s = "LVIII"
    print(Solution().romanToInt(s))
    assert (Solution().romanToInt(s) == 58)

    s = "MCMXCIV"
    print(Solution().romanToInt(s))
    assert (Solution().romanToInt(s) == 1994)