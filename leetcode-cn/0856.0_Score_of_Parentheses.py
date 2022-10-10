'''
stack, T: O(N), S: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了11.58% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了6.95% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
            else:
                t = 0
                while stack and stack[-1] != '(':
                    t += stack.pop()
                stack.pop()
                if t:
                    stack.append(t * 2)
                else:
                    stack.append(1)
        return sum(stack)
