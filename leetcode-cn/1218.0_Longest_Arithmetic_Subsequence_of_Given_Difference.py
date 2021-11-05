'''
执行用时：152 ms, 在所有 Python3 提交中击败了51.95% 的用户
内存消耗：24.9 MB, 在所有 Python3 提交中击败了17.53% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        ans = 0
        for x in arr:
            dp[x] = 1 + dp[x - difference]
            ans = max(ans, dp[x])

        return ans
        