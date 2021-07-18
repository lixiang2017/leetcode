'''
Time Limit Exceeded
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        achieve = [[0] * N for _ in range(M)]
        # init 
        for j in range(N):
            achieve[0][j] = points[0][j]
        # dp
        for i in range(1, M):
            for j in range(N):
                for k in range(N):
                    achieve[i][j] = max(achieve[i][j], points[i][j] + achieve[i - 1][k] - abs(j - k))
        
        return max(achieve[-1])
        