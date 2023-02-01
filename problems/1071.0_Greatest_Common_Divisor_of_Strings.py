'''
Runtime: 33 ms, faster than 79.41% of Python3 online submissions for Greatest Common Divisor of Strings.
Memory Usage: 13.8 MB, less than 98.52% of Python3 online submissions for Greatest Common Divisor of Strings.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        g = gcd(n1, n2)
        f1, f2 = n1 // g, n2 // g
        common = str1[: g]
        if common * f1 == str1 and common * f2 == str2:
            return common
        else:
            return ''
            