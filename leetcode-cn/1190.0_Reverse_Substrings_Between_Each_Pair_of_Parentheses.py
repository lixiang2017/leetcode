'''
approach: Stack
Time: O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了45.10% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了42.34% 的用户
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        part = ''
        for ch in s:
            if ch == '(':
                if part:
                    stack.append(part)
                    stack.append('(')
                else:
                    stack.append('(')
                part = ''
            elif ch == ')':
                segments = [part]
                part = ''
                while stack and stack[-1] != '(':
                    segments.append(stack.pop(-1))
                if stack:
                    stack.pop(-1) # pop '('
                straight = ''.join(segments[:: -1])[::-1]
                if straight:
                    stack.append(straight)  
            else:
                part += ch

        return ''.join(stack) + part
