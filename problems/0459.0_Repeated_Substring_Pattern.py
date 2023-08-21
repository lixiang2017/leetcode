'''
Runtime: 41 ms, faster than 91.38% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 16.5 MB, less than 46.01% of Python3 online submissions for Repeated Substring Pattern.
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if 0 == n % i and s[: i] * (n // i) == s and n // i > 1:
                return True
        return False
                
                