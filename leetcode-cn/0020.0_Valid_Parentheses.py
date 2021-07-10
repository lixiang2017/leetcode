'''
apprroach: Stack
Time: O(N)
Space: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了86.44% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了51.79% 的用户
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in  ['(', '{', '[']:
                stack.append(ch)
            elif stack:
                if ch == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif ch == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        
        return stack == []


'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.78% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.34% 的用户
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False

        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for ch in s:
            if ch in pairs:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack
        