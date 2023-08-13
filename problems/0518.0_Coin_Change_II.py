'''
Runtime 1472 ms Beats 8.6%
Memory 41.1 MB Beats 27.74%
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        n = len(coins)

        @cache
        def dfs(i, left):
            if i == n:
                return left == 0
            way = 0
            upper = left // coins[i]
            for c in range(upper + 1):
                way += dfs(i + 1, left - coins[i] * c)
            return way

        return dfs(0, amount)
        

'''
Runtime 5092 ms Beats 5.1% 
Memory 25.7 MB Beats 60.35%
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        dp = [[1] + [0] * (amount) for _ in range(n + 1)]
        for i in range(n):
            for left in range(1, amount + 1):
                upper = left // coins[i]
                for c in range(upper + 1):
                    dp[i + 1][left] += dp[i][left - coins[i] * c]

        return dp[n][amount]
