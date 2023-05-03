'''
stack
T: O(N)
S: O(N)

执行用时：68 ms, 在所有 Python3 提交中击败了34.51% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了5.31% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False
        stack = []
        for ch in s:
            if ch == 'c' and len(stack) > 1 and stack[-1] == 'b' and stack[-2] == 'a':
                stack.pop()
                stack.pop()
            else:
                stack.append(ch)
        return not stack

'''
执行用时：48 ms, 在所有 Python3 提交中击败了61.06% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.31% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False
        while 'abc' in s:
            s = s.replace('abc', '')
        return not s 

'''
执行用时：56 ms, 在所有 Python3 提交中击败了53.98% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.31% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False
        stack = []
        for o in map(ord, s):
            if o > ord('a') and (not stack or o - stack.pop() != 1):
                return False
            if o < ord('c'):
                stack.append(o)
        return not stack
        