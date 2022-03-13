'''
stack
T: O(N)
S: O(N)

Runtime: 59 ms, faster than 18.84% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 82.06% of Python3 online submissions for Valid Parentheses.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = {'(', '[', '{'}
        close2open = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in open_bracket:
                stack.append(ch)
            elif stack and stack[-1] == close2open[ch]:
                stack.pop()
            else:
                return False
        return stack == []

'''
replace

Runtime: 71 ms, faster than 6.17% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 82.06% of Python3 online submissions for Valid Parentheses.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            change = False
            for pair in ['[]', '()', '{}']:
                if pair in s:
                    change = True
                    s = s.replace(pair, '')
            if not change:
                break
        return s == ''
                
