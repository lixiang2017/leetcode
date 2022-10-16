'''
DP
T: O(N^2 * d)
S: O(N * d)

Runtime: 1685 ms, faster than 60.08% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
Memory Usage: 14 MB, less than 93.73% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[0] * n] + [[inf] * n for _ in range(d - 1)]
        m = 0
        for i, jd in enumerate(jobDifficulty):
            m = max(m, jd)
            dp[0][i] = m 
            
        for i in range(1, d):
            # from i-1 day state
            for j in range(i - 1, n - 1):
                m = 0
                # do delta jobs at day i
                for delta in range(1, n - j):
                    m = max(m, jobDifficulty[j + delta])
                    dp[i][j + delta] = min(dp[i][j + delta], dp[i - 1][j] + m)
                    
        return dp[d - 1][n - 1] if dp[d - 1][n - 1] != inf else -1
