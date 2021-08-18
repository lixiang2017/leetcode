'''
DP
Time: O(N)
Space: O(N)

59 / 59 个通过测试用例
状态：通过
执行用时: 3768 ms
内存消耗: 38.2 MB
提交时间：1 小时前
'''
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        # dp[x][y][z]
        ## x: times of A
        ## y: count for continuous L in the tail
        ## z: length of string - 1
        dp = [[[0] * n for _ in range(3)] for _ in range(2)]
        # init state
        ## only P
        dp[0][0][0] = 1
        ## only L
        dp[0][1][0] = 1
        ## only one A
        dp[1][0][0] = 1

        for i in range(1, n):
            # if the i-th day is P
            for j in range(2):
                dp[j][0][i] += (dp[j][0][i-1] + dp[j][1][i-1] + dp[j][2][i-1]) % MOD

            # if the i-th day is A
            dp[1][0][i] += (dp[0][0][i-1] + dp[0][1][i-1] + dp[0][2][i-1]) % MOD

            # if the i-th day is L
            for a in range(2):
                for k in range(1, 3):
                    dp[a][k][i] += dp[a][k-1][i-1] % MOD

        
        for a in range(2):
            for l in range(3):
                ans += dp[a][l][n - 1]

        return ans % MOD
