'''
DP, T: O(N), S: O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了5.25% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了69.53% 的用户
通过测试用例：283 / 283
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return dp[-1]

'''
DP, T: O(N), S: O(1)

执行用时：52 ms, 在所有 Python3 提交中击败了10.02% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了92.49% 的用户
通过测试用例：283 / 283
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        a, b = cost[0], cost[1]
        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]
        return b

'''
DP, no need to append 
T: O(N), S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了20.90% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了58.42% 的用户
通过测试用例：283 / 283
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = cost[0], cost[1]
        for i in range(2, n):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)



'''
DP, no need to append, in place
T: O(N), S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了42.77% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.27% 的用户
通过测试用例：283 / 283
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2], cost[-1])



