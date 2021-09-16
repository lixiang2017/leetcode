'''
bitwise

执行用时：40 ms, 在所有 Python3 提交中击败了79.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了57.27% 的用户
通过测试用例：507 / 507
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c, sub = [0] * 9, [0] * 9, [0] * 9
        for i in range(9):
            for j in range(9):
                if '.' == board[i][j]:
                    continue
                x = ord(board[i][j]) - ord('0')
                b = (1 << x)
                # r
                if r[i] & b:
                    return False
                r[i] |= b
                # c
                if c[j] & b:
                    return False
                c[j] |= b
                # sub
                idx = (i // 3) * 3 + (j // 3)
                if sub[idx] & b:
                    return False
                sub[idx] |= b
        return True
