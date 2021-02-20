'''
apporach: Hash Table
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 60.41 % of python submissions.

'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Symbol2Value = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000,
        }
        
        integer = 0
        integer = sum(Symbol2Value[symbol] for symbol in s)
        if "IV" in s or "IX" in s:
            integer -= 2
        if "XL" in s or "XC" in s:
             integer -= 20
        if "CD" in s or "CM" in s:
             integer -= 200
        
        return integer
    