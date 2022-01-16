'''
T: O(N)
S: O(1)

Runtime: 55 ms, faster than 18.44% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14.3 MB, less than 57.28% of Python3 online submissions for String to Integer (atoi).
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -(1 << 31), (1 << 31) - 1
        ans = i = 0
        isNegative = False
        n = len(s)
        # ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        # read sign and digits
        ## read sign
        if i < n and s[i] in '-+':
            if s[i] == '-':
                isNegative = True
            i += 1
        ## read digits 
        while i < n and s[i].isdigit():
            ans *= 10
            ans += ord(s[i]) - ord('0')
            if isNegative and -ans <= MIN:
                return MIN
            if not isNegative and ans >= MAX:
                return MAX
            i += 1
             
        return -ans if isNegative else ans
