'''
Your code took 2 milliseconds — faster than 100.00% in Python
'''

class Solution:
    def solve(self, s):
        ans = ''
        cnt = 0
        for ch in s:
            if 'a' <= ch <= 'z':
                ans += ch * cnt
                cnt = 0
            else:
                cnt *= 10
                cnt += int(ch)

        return ans
        # return ''.join(int(s[i]) * s[i + 1] for i in range(0, len(s), 2))


'''
Your code took 2 milliseconds — faster than 100.00% in Python
'''
class Solution:
    def solve(self, s):
        output = ''
        num = ''
        for ch in s:
            if ch.isalpha():
                output += ch * int(num)
                num = ''
            else:
                num += ch

        return output        