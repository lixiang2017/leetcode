'''
simulation
T: O(N*N + 2*N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了44.38% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了55.03% 的用户
通过测试用例：24 / 24
'''
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find Rook
        r = c = 0
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'R':
                    r, c = i, j
                    break 
        ans = 0
        # four directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc 
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':
                    break
                if board[nr][nc] == 'p':
                    ans += 1
                    break 
                nr += dr 
                nc += dc 

        return ans 
