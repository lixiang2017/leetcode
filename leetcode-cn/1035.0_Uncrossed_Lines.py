'''
DP,T:O(MN),S:O(MN)

执行用时：188 ms, 在所有 Python3 提交中击败了84.41% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了82.03% 的用户
'''


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(M):
                if nums2[i] == nums1[j]:
                    dp[i + 1][j + 1] = max(1 + dp[i][j], dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return max(dp[-1])
