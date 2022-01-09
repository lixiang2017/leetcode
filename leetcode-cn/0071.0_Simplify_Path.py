'''
stack

执行用时：36 ms, 在所有 Python3 提交中击败了53.79% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了69.10% 的用户
通过测试用例：256 / 256
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '..' and stack:
                stack.pop()
            elif part not in ('', '.', '..'):
                stack.append(part)

        return '/' + '/'.join(stack)

