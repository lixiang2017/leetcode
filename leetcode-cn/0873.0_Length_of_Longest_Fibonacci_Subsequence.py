'''
画图好好分析状态如何转移的，我居然很顺利做出来了.
画个二维表格，手动模拟状态如何转移的就清晰了

T: O(N^2)
S: O(N^2)

执行用时：1132 ms, 在所有 Python3 提交中击败了83.41% 的用户
内存消耗：22.9 MB, 在所有 Python3 提交中击败了32.51% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num2idx = {x : i for i, x in enumerate(arr)}
        n = len(arr)
        # arr[i] -> arr[j], only prev_idx < i < j is valid
        dp = [[2] * n for _ in range(n)]
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                prev = arr[j] - arr[i]
                if prev in num2idx and num2idx[prev] < i:
                    prev_idx = num2idx[prev]
                    dp[i][j] = dp[prev_idx][i] + 1
                    ans = max(ans, dp[i][j])
        return ans 


'''
执行用时：1140 ms, 在所有 Python3 提交中击败了82.51% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了63.90% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num2idx = {x : i for i, x in enumerate(arr)}
        n = len(arr)
        # arr[i] -> arr[j], only prev_idx < i < j is valid
        dp = defaultdict(lambda: 2)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                prev = arr[j] - arr[i]
                if prev in num2idx and num2idx[prev] < i:
                    prev_idx = num2idx[prev]
                    dp[i, j] = dp[prev_idx, i] + 1
                    ans = max(ans, dp[i, j])
        return ans 

