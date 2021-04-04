'''
224 / 231 个通过测试用例
状态：超出时间限制
提交时间：几秒内

Brute Force
Time: O(N^3)
Space: O(N + N) = O(N)
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValid(x):
            stack = []
            for token in x:
                if '(' == token:
                    stack.append(token)
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []
        
        if len(s) < 2: return 0
        N = len(s)
        for i in range(N if N % 2 == 0 else N - 1, 0, -2):
            for j in range(N - i + 1):
                if isValid(s[j: j + i]):
                    return i
        return 0

