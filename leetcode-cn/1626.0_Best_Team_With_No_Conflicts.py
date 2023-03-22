'''
Sort + DP

执行用时：1704 ms, 在所有 Python3 提交中击败了44.19% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了98.84% 的用户
'''
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = [(a, s) for a, s in zip(ages, scores)]
        pairs.sort()
        dp = [0] * n
        for i in range(n):
            dp[i] = pairs[i][1]
            for j in range(i):
                if pairs[j][1] <= pairs[i][1]:
                    dp[i] = max(dp[i], dp[j] + pairs[i][1])
        return max(dp)
