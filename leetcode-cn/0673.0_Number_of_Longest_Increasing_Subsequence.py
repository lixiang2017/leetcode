'''
DP + Hash Table
T: O(N^2 + N)
每一个元素跟之前所有元素进行比较，并更新当前元素位置的计数。

执行用时：2180 ms, 在所有 Python3 提交中击败了5.09% 的用户
内存消耗：139.1 MB, 在所有 Python3 提交中击败了5.09% 的用户
通过测试用例：223 / 223
'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        # idx -> {len: cnt}
        pos2cnt = [Counter([1]) for _ in range(N)]
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    pos2cnt[i][dp[j] + 1] += pos2cnt[j][dp[j]]
                    dp[i] = max(dp[i], dp[j] + 1)

        max_len = max(dp)
        ans = 0
        for c in pos2cnt:
            ans += c[max_len]
        return ans

