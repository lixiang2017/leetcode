'''
执行用时：36 ms, 在所有 Python3 提交中击败了68.37% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.82% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def interpret(self, command: str) -> str:
        decode = command.replace('()', 'o').replace('(al)', 'al')
        return decode


'''
执行用时：36 ms, 在所有 Python3 提交中击败了68.37% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了24.44% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def interpret(self, command: str) -> str:
        decode = []
        i, n = 0, len(command)
        while i < n:
            if command[i] == 'G':
                decode.append('G')
                i += 1
            elif command[i + 1] == ')':
                decode.append('o')
                i += 2
            else:
                decode.append('al')
                i += 4
        return ''.join(decode)
