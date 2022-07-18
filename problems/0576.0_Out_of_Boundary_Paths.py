'''
DFS + memoization

Runtime: 136 ms, faster than 81.84% of Python3 online submissions for Out of Boundary Paths.
Memory Usage: 20.4 MB, less than 17.39% of Python3 online submissions for Out of Boundary Paths.
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(move, r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 1
            if move == 0:
                return 0
            p = 0
            p += dfs(move - 1, r - 1, c)
            p += dfs(move - 1, r + 1, c)
            p += dfs(move - 1, r, c - 1)
            p += dfs(move - 1, r, c + 1)
            return p % MOD 
        
        return dfs(maxMove, startRow, startColumn)



'''
maxMove, 所以真实的 move 取值可以是 for move in range(1, maxMove + 1)


Runtime: 217 ms, faster than 45.27% of Python3 online submissions for Out of Boundary Paths.
Memory Usage: 33.6 MB, less than 5.37% of Python3 online submissions for Out of Boundary Paths.
'''
class Solution:
    
    MOD = 10 ** 9 + 7
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return sum(self.path_cnt(m, n, move, startRow, startColumn) for move in range(1, maxMove + 1)) % self.MOD 
        
    @cache
    def path_cnt(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:  
        if not (0 <= startRow < m and 0 <= startColumn < n):
            return 0
        if maxMove == 0:
            return 0
        if maxMove == 1:
            if m == 1 and n == 1 and startRow == 0 and startColumn == 0:
                return 4
            if m == 1:
                return 2 + int(startColumn in [0, n - 1])
            if n == 1:
                return 2 + int(startRow in [0, m - 1])
            if startRow in [0, m - 1]:
                return 1 + int(startColumn in [0, n - 1])
            if startColumn in [0, n - 1]:
                return 1 + int(startRow in [0, m - 1])
            return 0

        up = self.path_cnt(m, n, maxMove - 1, startRow - 1, startColumn)
        down = self.path_cnt(m, n, maxMove - 1, startRow + 1, startColumn)
        left = self.path_cnt(m, n, maxMove - 1, startRow, startColumn - 1)
        right = self.path_cnt(m, n, maxMove - 1, startRow, startColumn + 1)
        return (up + down + left + right) % self.MOD 
   

'''
Input
1
1
5
0
0
Output
3
Expected
4
'''


'''
DP
农村包围城市

Runtime: 266 ms, faster than 32.99% of Python3 online submissions for Out of Boundary Paths.
Memory Usage: 18.5 MB, less than 44.50% of Python3 online submissions for Out of Boundary Paths.
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        path = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(1 + maxMove)]
        # init for move = 0
        for j in range(1, n + 1):
            path[0][0][j] = 1
            path[0][m + 1][j] = 1
        for i in range(1, m + 1):
            path[0][i][0] = 1
            path[0][i][n + 1] = 1
        # DP
        for move in range(1, maxMove + 1):
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    path[move][i][j] = (path[move-1][i-1][j] + path[move-1][i+1][j] + path[move-1][i][j-1] + path[move-1][i][j+1]) % MOD 
                    
        ans = 0
        for move in range(1, maxMove + 1):
            ans += path[move][startRow + 1][startColumn + 1] 
            ans %= MOD
        return ans 
    
            
'''
压缩成两维

Runtime: 432 ms, faster than 16.11% of Python3 online submissions for Out of Boundary Paths.
Memory Usage: 14.3 MB, less than 84.91% of Python3 online submissions for Out of Boundary Paths.
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        path = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(2)]
        # init for move = 0
        for j in range(1, n + 1):
            path[0][0][j] = 1
            path[0][m + 1][j] = 1
        for i in range(1, m + 1):
            path[0][i][0] = 1
            path[0][i][n + 1] = 1
        # DP
        ans = 0
        for move in range(1, maxMove + 1):
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    path[move & 1][i][j] = (path[(move-1) & 1][i-1][j] + \
                                            path[(move-1) & 1][i+1][j] + \
                                            path[(move-1) & 1][i][j-1] + \
                                            path[(move-1) & 1][i][j+1]) % MOD 
                    if i == startRow + 1 and j == startColumn + 1:
                        ans += path[move & 1][i][j]
                        ans %= MOD 
            # clear init 
            if move == 1:
                for j in range(1, n + 1):
                    path[0][0][j] = 0
                    path[0][m + 1][j] = 0
                for i in range(1, m + 1):
                    path[0][i][0] = 0
                    path[0][i][n + 1] = 0               
        return ans 
            



