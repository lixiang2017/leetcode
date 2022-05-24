'''
DP 完全背包，求组合数。先遍历硬币

执行用时：120 ms, 在所有 Python3 提交中击败了90.24% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了37.81% 的用户
通过测试用例：28 / 28
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for j in range(c, amount + 1):
                dp[j] += dp[j - c]
        return dp[-1]


'''
DFS

执行用时：836 ms, 在所有 Python3 提交中击败了5.62% 的用户
内存消耗：313.1 MB, 在所有 Python3 提交中击败了5.03% 的用户
通过测试用例：28 / 28
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0
            return dfs(i, total + coins[i]) + dfs(i + 1, total)
        
        return dfs(0, 0)
