'''
DP
T: O(MN)
S: O(MN)

Runtime: 32 ms, faster than 69.60% of Python3 online submissions for Unique Paths.
Memory Usage: 14.1 MB, less than 86.91% of Python3 online submissions for Unique Paths.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0] * (n + 1) for _ in range(m + 1)]
        path[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[-1][-1]

'''
DP

Runtime: 28 ms, faster than 88.26% of Python3 online submissions for Unique Paths.
Memory Usage: 14 MB, less than 99.61% of Python3 online submissions for Unique Paths.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]



'''
DP

Runtime: 44 ms, faster than 65.78% of Python3 online submissions for Unique Paths.
Memory Usage: 13.8 MB, less than 73.91% of Python3 online submissions for Unique Paths.
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(m - 1):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]
