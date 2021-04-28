'''
approach: DP
Time: O(MN)
Space: O(MN)

You are here!
Your runtime beats 49.87 % of python3 submissions.
You are here!
Your memory usage beats 61.16 % of python3 submissions.
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N =  len(obstacleGrid), len(obstacleGrid[0]) if obstacleGrid else 0
        dp = [[0] * N for _ in range(M)]
        if obstacleGrid[0][0]:
            return 0
        else:
            dp[0][0] = 1
        # first row
        for j in range(1, N):
            if obstacleGrid[0][j]:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, M):
            for j in range(N):
                if j == 0:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if obstacleGrid[i][j]:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[M - 1][N - 1]
