'''
DP, T: O(N), S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了91.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.63% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])


'''
执行用时：48 ms, 在所有 Python3 提交中击败了24.23% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了29.85% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            dp = [min(dp[j - 1], dp[j - 2]) + c for j, c in enumerate(costs[i])]
        return min(dp)
        