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


'''
approach: DP, general approach, no edge cases out of for loop
Time: O(MN)
Space: O(MN)

You are here!
Your runtime beats 93.69 % of python3 submissions.
You are here!
Your memory usage beats 84.00 % of python3 submissions.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N =  len(obstacleGrid), len(obstacleGrid[0]) if obstacleGrid else 0
        dp = [[0] * N for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                # start point
                elif 0 == i and 0 == j:
                    dp[i][j] = 1
                # first row
                elif 0 == i:
                    dp[i][j] = dp[i][j - 1]
                # first column
                elif 0 == j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[M - 1][N - 1]

