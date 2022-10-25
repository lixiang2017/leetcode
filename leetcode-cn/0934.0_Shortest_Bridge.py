'''
执行用时：3620 ms, 在所有 Python3 提交中击败了5.44% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了81.93% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        one, another = set(), set()
        # find one 1 for one
        i1 = j1 = -1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    i1 = i 
                    j1 = j
                    break  
            if i1 != -1:
                break 
        # BFS for one 
        one.add((i1, j1))
        q = deque([(i1, j1)])
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in one and grid[ni][nj] == 1:
                    one.add((ni, nj))
                    q.append((ni, nj))
        # find one 1 for another 
        i2 = j2 = -1
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1 and (i, j) not in one:
                    i2 = i 
                    j2 = j 
                    break 
            if i2 != -1:
                break 
        # BFS for another
        another.add((i2, j2))
        q = deque([(i2, j2)])
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in another and grid[ni][nj] == 1:
                    another.add((ni, nj))
                    q.append((ni, nj))
        
        ans = 2 * n
        for i1, j1 in one:
            for i2, j2 in another:
                b = abs(i1 - i2) + abs(j1 - j2) - 1
                ans = min(ans, b)
                if ans == 1:
                    return 1
        return ans 

