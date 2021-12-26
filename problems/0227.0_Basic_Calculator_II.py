'''
Runtime: 80 ms, faster than 78.40% of Python3 online submissions for Basic Calculator II.
Memory Usage: 59.8 MB, less than 5.44% of Python3 online submissions for Basic Calculator II.
'''
class Solution:
    def calculate(self, s: str) -> int:
        return eval(s.replace('/', '//'))
        