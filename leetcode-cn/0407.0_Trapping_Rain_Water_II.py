'''
农村包围城市
从边缘开始处理，逐步处理到中心
heapq
T: O(MNlog(M+N))
S: O(MN)

执行用时：212 ms, 在所有 Python3 提交中击败了93.48% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了76.52% 的用户
通过测试用例：42 / 42
'''
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        hm = heightMap
        M, N = len(hm), len(hm[0])
        if M < 3 or N < 3:
            return 0

        pq = []
        visited = [[0] * N for _ in range(M)]
        for i in range(M):
            heapq.heappush(pq, (hm[i][0], i * N))
            heapq.heappush(pq, (hm[i][N-1], i * N + N - 1))
            visited[i][0] = visited[i][N-1] = 1
        for j in range(1, N - 1):
            heapq.heappush(pq, (hm[0][j], j))
            heapq.heappush(pq, (hm[M-1][j], (M - 1) * N + j))
            visited[0][j] = visited[M-1][j] = 1

        ans = 0
        while pq:
            # height, position
            h, p = heappop(pq)
            x, y = p // N, p % N
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < M and 0 < ny < N and not visited[nx][ny]:
                    if hm[nx][ny] < h:
                        ans += h - hm[nx][ny]
                    visited[nx][ny] = 1
                    heapq.heappush(pq, (max(h, hm[nx][ny]), nx * N + ny))

        return ans
