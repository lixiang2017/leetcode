'''
backtracking + hash table * 3

执行用时：60 ms, 在所有 Python3 提交中击败了61.75% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了78.60% 的用户
通过测试用例：9 / 9
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def backtracking(row_idx: int, col: set, diag: set, anti_diag: set, cols: list):
            if row_idx == n:
                board = []
                for i, cc in enumerate(cols):
                    line = ['.'] * n 
                    line[cc] = 'Q'
                    board.append(''.join(line))
                ans.append(board)
                return 
                
            # current row_idx, check every column
            for c in range(n):
                if c in col or row_idx + c in diag or row_idx - c in anti_diag:
                    continue
                # can put, next row
                backtracking(row_idx + 1, col|{c}, diag|{row_idx+c}, anti_diag|{row_idx-c}, cols + [c])

        backtracking(0, set(), set(), set(), [])
        return ans 


'''
执行用时：52 ms, 在所有 Python3 提交中击败了72.13% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了65.46% 的用户
通过测试用例：9 / 9
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def backtracking(row_idx: int, col: set, diag: set, anti_diag: set, cols: list):
            if row_idx == n:
                ans.append(['.' * cc + 'Q' + '.' * (n - 1 - cc) for cc in cols])
                return 

            # current row_idx, check every column
            for c in range(n):
                if c in col or row_idx + c in diag or row_idx - c in anti_diag:
                    continue
                # can put, next row
                backtracking(row_idx + 1, col|{c}, diag|{row_idx+c}, anti_diag|{row_idx-c}, cols + [c])

        backtracking(0, set(), set(), set(), [])
        return ans 

