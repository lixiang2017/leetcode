'''
DP
T: O(N^2)
S: O(N)

22 / 30 个通过测试用例
状态：超出时间限制

这种写法最后必须要使用max(dp)，而不能使用dp[-1]. 因为，dp[j]表示的是一定会选择job[j]
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        pairs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        pairs.sort()
        dp = [0] * n 
        dp[0] = pairs[0][2]
        # i ... j
        for j in range(1, n):
            # just do j 
            dp[j] = pairs[j][2]
            for i in range(j):
                if pairs[i][1] <= pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + pairs[j][2])
        return max(dp)

'''
序列DP + sort + binary search
T: O(NlogN)
S: O(N)

用左端点（开始时间）排序，无法使用二分。
必须用右端点（结束时间）排序，才能使用二分。由于按照结束时间排序，前 j 个工作中的任意一个都不会与第 i 个工作的时间重叠。

https://leetcode.cn/problems/maximum-profit-in-job-scheduling/solution/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-zkcg/


执行用时：144 ms, 在所有 Python3 提交中击败了82.20% 的用户
内存消耗：31 MB, 在所有 Python3 提交中击败了14.82% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        pairs = [[s, e, p] for s, e, p in zip(startTime, endTime, profit)]
        pairs.sort(key=lambda p: p[1])
        startTime, endTime, profit = zip(*pairs)
        dp = [0] * (len(profit) + 1)
        for i in range(len(profit)):
            idx = bisect_right(endTime, startTime[i])
            dp[i + 1] = max(dp[i], dp[idx] + profit[i])
        return dp[-1]

