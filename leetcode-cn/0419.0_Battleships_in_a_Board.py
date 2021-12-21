'''
会修改board
T: O(MN*max(M,N)),S: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了85.71% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了97.32% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if 'X' == board[i][j]:
                    ans += 1
                    ii, jj = i, j + 1
                    while ii < m and board[ii][j] == 'X':
                        board[ii][j] = '.'
                        ii += 1
                    while jj < n and board[i][jj] == 'X':
                        board[i][jj] = '.'
                        jj += 1
        return ans

'''
不修改board
战舰头'X' 上方与左侧都是 '.'
只记录战舰头，T:O(MN), S:O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了95.98% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了88.39% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
                    continue
                if board[i][j] == 'X':
                    ans += 1
        return ans


'''
不修改board
one if, 只记录战舰头，T:O(MN), S:O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了64.29% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了83.04% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not ((i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X')) \
                        and board[i][j] == 'X':
                    ans += 1
        return ans

'''
# 只记录战舰尾，战舰尾'X' 下方与右侧都是'.'

执行用时：36 ms, 在所有 Python3 提交中击败了64.29% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了76.79% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i < m - 1 and board[i + 1][j] == 'X') or (j < n - 1 and board[i][j + 1] == 'X'):
                    continue
                if board[i][j] == 'X':
                    ans += 1
        return ans


'''
one if # 只记录战舰尾，战舰尾'X' 下方与右侧都是'.'

执行用时：56 ms, 在所有 Python3 提交中击败了7.59% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了76.79% 的用户
通过测试用例：27 / 27
'''

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not ((i < m - 1 and board[i + 1][j] == 'X') or (j < n - 1 and board[i][j + 1] == 'X')) and \
                        board[i][j] == 'X':
                    ans += 1
        return ans


'''
UF

执行用时：48 ms, 在所有 Python3 提交中击败了7.59% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了5.36% 的用户
通过测试用例：27 / 27
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py 

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0
        uf = UF(m * n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and i < m-1 and board[i + 1][j] == 'X':
                    uf.union(i * n + j, (i + 1) * n + j)
                if board[i][j] == 'X' and j < n-1 and board[i][j + 1] == 'X':
                    uf.union(i * n + j, i * n + j + 1)
        ans = len(set(uf.find(i * n + j) for i in range(m) for j in range(n) if board[i][j] == 'X'))
        return ans

