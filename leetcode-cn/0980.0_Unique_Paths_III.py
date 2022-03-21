'''
backtracking
这样暴力就过了，其实还可以用位操作压缩一下。


执行用时：64 ms, 在所有 Python3 提交中击败了33.01% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了18.18% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        paths = set()
        obstacle = set()
        start, end = None, None
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                # obstacles
                if x == -1:
                    obstacle.add((i, j))
                elif x == 1:
                    start = (i, j)
                elif x == 2:
                    end = (i, j)

        empty = m * n - 2 - len(obstacle)

        def backtracking(path, cur_pos):
            if cur_pos == end:
                if len(path) == empty + 2:
                    paths.add(tuple(path))
                return 
            i, j = cur_pos 
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in obstacle and (ni, nj) != start:
                    if (ni, nj) not in path:
                        backtracking(path + [(ni, nj)], (ni, nj))

        backtracking([start], start)
        return len(paths)


'''
backtracking
其实没必要把经过的路径path,传到参数里。传到参数里，还得花费O(N)去检查有没有访问过。
可以通过改变grid[r][c]的值为-1代表访问过，之后再还原。类似染色。

T: O(4 ^ (M*N))。从每个节点出发，都会有四个方向，四种可能性。
S: O(M*N), 栈的深度。所有节点的个数。

执行用时：56 ms, 在所有 Python3 提交中击败了57.42% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了65.07% 的用户
通过测试用例：39 / 39
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        self.paths = obstacle = 0 
        start, end = None, None
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                # obstacles
                if x == -1:
                    obstacle += 1
                elif x == 1:
                    start = (i, j)
                elif x == 2:
                    end = (i, j)

        todo = m * n - obstacle
        def neighbours(r, c):
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] % 2 == 0:
                    yield nr, nc 

        def backtracking(todo, x, y):
            todo -= 1
            if todo < 0:
                return 
            if x == end[0] and y == end[1]:
                if todo == 0:
                    self.paths += 1
                return 

            for nx, ny in neighbours(x, y):
                grid[x][y] = -1
                backtracking(todo, nx, ny)
                grid[x][y] = 0

        backtracking(todo, start[0], start[1])
        return self.paths



