'''
Runtime: 134 ms, faster than 5.08% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 31.19% of Python3 online submissions for Roman to Integer.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000,
        }
        ans = sum(value[ch] for ch in s)
        ans -= (s.count('IV') * 2 + s.count('IX') * 2)
        ans -= (s.count('XL') * 20 + s.count('XC') * 20)
        ans -= (s.count('CD') * 200 + s.count('CM') * 200)
        return ans 
        