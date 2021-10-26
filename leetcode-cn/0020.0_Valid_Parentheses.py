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


'''
stack, T: O(N), S: O(N)

执行用时：32 ms, 在所有 Python3 提交中击败了70.28% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.65% 的用户
通过测试用例：91 / 91
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        left = {'(', '[', '{'}
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if stack and pair[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack



'''
执行用时：48 ms, 在所有 Python3 提交中击败了8.22% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.25% 的用户
通过测试用例：91 / 91
'''
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return s == ''
        