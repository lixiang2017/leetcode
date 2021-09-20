'''
DP + Hash Table
T: O(N^2 + N)
s: O(N^2)
每一个元素i跟之前所有元素[0..i-1]进行比较，并更新当前元素位置的计数pos2cnt[i]。

dp[i] 表示以nums[i]为结尾的所有递增子序列的最长的长度。如果没有上升，可以不用管。
pos2cnt[i] 表示以nums[i]为结尾所有递增子序列的情况，为一计数字典。长度->个数

下图二维DP表。
dp数组把该二维表进行了压缩，dp[i]表示每一列的最大值。
遍历顺序：从左向右遍历每一列。每一列中从上到下，从下到上均可。
下三角区域不用计算。
对角线中dp均为1，计数初始均为Counter([1]). （仅表示当前每个元素自己表示的序列，长度是1，个数也是1.）

如果发现了上升，长度变为dp[j] + 1，加上之前的个数pos2cnt[j][dp[j]]。

       19  13  23   54
    19  1 (1)  2    2
	13     1   2    2
	23         1    3
	54              1


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

