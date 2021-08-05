'''
博弈论
DP,T:(N^2),S:O(N^2)

执行用时：24 ms, 在所有 Python3 提交中击败了99.64% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了59.15% 的用户
'''
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        if N % 2 == 0:
            return True

        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = nums[i]

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][N - 1] >= 0
