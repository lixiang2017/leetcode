'''
approach: DP
Time: O(N^2)
Space: O(N^2)

执行用时：1308 ms, 在所有 Python3 提交中击败了31.79%的用户
内存消耗：45.4 MB, 在所有 Python3 提交中击败了10.87%的用户
'''


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        N = len(stones)
        dp = [[False] * N for _ in range(N)]
        dp[0][0] = True
        for i in range(1, N):
            if stones[i] - stones[i - 1] > i:
                return False
        
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break
            
                # dp[i][k] = dp[i][k] or dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if dp[N - 1][k]:
                    return True

        return False
