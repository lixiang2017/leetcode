'''
stack
T: O(2N)
S: O(N)

Runtime: 31 ms, faster than 92.86% of Python3 online submissions for Simplify Path.
Memory Usage: 14 MB, less than 32.22% of Python3 online submissions for Simplify Path.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for part in parts:
            if part in {'.', ''}:
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
                
        return '/' + '/'.join(stack)
