'''
ref:
https://leetcode.cn/problems/fHi6rV/solution/by-v5qyy4q65w-66s1/

执行用时：100 ms, 在所有 Python3 提交中击败了7.84% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了27.45% 的用户
通过测试用例：154 / 154
'''
class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        m, n = len(chessboard), len(chessboard[0])
        dirs = [[-1, 1], [1, -1], [1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]

        def find(i, j, d, visited):
            res = set()
            while True:
                i += dirs[d][0]
                j += dirs[d][1]
                if not (0 <= i < m and 0 <= j < n) or chessboard[i][j] == '.':
                    return set()
                if (i, j) not in visited and chessboard[i][j] == 'O':
                    res.add((i, j))
                else:
                    return res 
        
        def bfs(i, j):
            q = {(i, j)}
            visited = {(i, j)}
            while q:
                next_q = set()
                for r, c in q:
                    for d in range(8):
                        new = find(r, c, d, visited)
                        next_q |= new 
                        visited |= new 
                q = next_q
            return len(visited) - 1

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, bfs(i, j))
        return ans 

'''
if chessboard[i][j] == '.':
	
执行用时：68 ms, 在所有 Python3 提交中击败了25.49% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了9.80% 的用户
通过测试用例：154 / 154
'''
class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        m, n = len(chessboard), len(chessboard[0])
        dirs = [[-1, 1], [1, -1], [1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]

        def find(i, j, d, visited):
            res = set()
            while True:
                i += dirs[d][0]
                j += dirs[d][1]
                if not (0 <= i < m and 0 <= j < n) or chessboard[i][j] == '.':
                    return set()
                if (i, j) not in visited and chessboard[i][j] == 'O':
                    res.add((i, j))
                else:
                    return res 
        
        def bfs(i, j):
            q = {(i, j)}
            visited = {(i, j)}
            while q:
                next_q = set()
                for r, c in q:
                    for d in range(8):
                        new = find(r, c, d, visited)
                        next_q |= new 
                        visited |= new 
                q = next_q
            return len(visited) - 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == '.':
                    ans = max(ans, bfs(i, j))
        return ans 


