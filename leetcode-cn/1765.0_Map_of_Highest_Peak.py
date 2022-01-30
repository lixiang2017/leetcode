'''

'''
'''
BFS

执行用时：2192 ms, 在所有 Python3 提交中击败了20.93% 的用户
内存消耗：77.2 MB, 在所有 Python3 提交中击败了49.61% 的用户
通过测试用例：59 / 59

[[0,1],
 [0,0]]

[[0,0,1],
 [1,0,0],
 [0,0,0]]
'''

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        q = deque()
        for i, row in enumerate(isWater):
            for j, isw in enumerate(row):
                if isw == 1:
                    q.append((i, j))
                    height[i][j] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    # find low
                    low = height[x][y]
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = nx + di, ny + dj 
                        if 0 <= ni < m and 0 <= nj < n and height[ni][nj] != -1:
                            low = min(low, height[ni][nj])
                    height[nx][ny] = low + 1
                    q.append((nx, ny))

        return height

