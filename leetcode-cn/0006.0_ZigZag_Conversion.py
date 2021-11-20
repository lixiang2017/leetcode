'''
simulation

执行用时：52 ms, 在所有 Python3 提交中击败了64.16% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了30.22% 的用户
通过测试用例：1157 / 1157
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if 1 == numRows:
            return s

        rows = [[] for _ in range(numRows)]
        down = True
        r = 0
        for i, ch in enumerate(s):
            rows[r].append(ch)
            if down:
                r += 1
            else:
                r -= 1

            if r == numRows:
                r -= 2
                down = False
            if r == -1:
                r += 2
                down = True

        return ''.join([''.join(row) for row in rows])

