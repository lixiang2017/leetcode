'''
BFS
need to set grid[ii][jj] = 0 early!

执行用时：88 ms, 在所有 Python3 提交中击败了70.44% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了70.44% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        boundary = deque()
        for i in [0, m - 1]:
            for j in range(n):
                if 1 == grid[i][j]:
                    boundary.append(i * n + j)
                    grid[i][j] = 0
        for j in [0, n - 1]:
            for i in range(m):
                if 1 == grid[i][j]:
                    boundary.append(i * n + j)  
                    grid[i][j] = 0              

        while boundary:
            idx = boundary.popleft()
            i, j = divmod(idx, n)     
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < m and 0 <= jj < n and 1 == grid[ii][jj]:
                    boundary.append(ii * n + jj)
                    grid[ii][jj] = 0

        return sum(1 == grid[i][j] for i in range(1, m - 1) for j in range(1, n - 1))

'''
BFS

执行用时：120 ms, 在所有 Python3 提交中击败了39.49% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了5.09% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = set()
        boundary = deque()
        # set boundary cell 1 to 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.add(i * n + j)
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        boundary.append(i * n + j)
                        grid[i][j] = 0
                        
        while boundary:
            idx = boundary.popleft()
            i, j = divmod(idx, n)
            ones.discard(idx)
            seen.add(idx)
            # wrong
            # for ii in range(i - 1, i + 2):
            #    for jj in range(j - 1, j + 2):
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1 and ii * n + jj not in seen:
                    boundary.append(ii * n + jj)
                    grid[ii][jj] = 0

        return len(ones)



'''
BFS

执行用时：116 ms, 在所有 Python3 提交中击败了40.18% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了5.09% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = set()
        boundary = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.add(i * n + j)
                    if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                        boundary.append(i * n + j)
                        grid[i][j] = 0

        while boundary:
            idx = boundary.popleft()
            i, j = divmod(idx, n)
            ones.discard(idx)
            # wrong
            # for ii in range(i - 1, i + 2):
            #    for jj in range(j - 1, j + 2):
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                # wrong
                # if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1 and ii * n + jj not in ones:
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                    boundary.append(ii * n + jj)
                    grid[ii][jj] = 0

        return len(ones)


