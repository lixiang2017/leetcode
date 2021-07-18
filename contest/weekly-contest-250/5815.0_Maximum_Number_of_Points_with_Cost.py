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


'''
DP,T:O(3MN),S:O(N)

执行用时：644 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：32.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M, N = len(points), len(points[0])
        dp = [0] * N
        for i in range(M):
            for j in range(N):
                dp[j] += points[i][j]
            for j in range(1, N):
                dp[j] = max(dp[j], dp[j - 1] - 1)
            for j in range(N - 2, -1, -1):
                dp[j] = max(dp[j], dp[j + 1] - 1)
        return max(dp)
