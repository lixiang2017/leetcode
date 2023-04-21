'''
39 / 45 test cases passed.
	Status: Time Limit Exceeded

这一版超时了是因为 DFS中第一维度的数字太大了。
10000 * 100 * 100 = 10 ** 8
'''
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(cur_profit, i, member):
            if member > n :
                return 0
            if i >= m:
                if cur_profit >= minProfit:
                    return 1
                return 0
            # choose
            c1 = dfs(cur_profit + profit[i], i + 1, member + group[i])
            # not choose
            c2 = dfs(cur_profit, i + 1, member)
            return (c1 + c2) % MOD 
            
        return dfs(0, 0, 0)



'''
DFS + memo
使用 min(minProfit, cur_profit + profit[i]) 优化，降低第一维度的数值。
取得高于 minProfit 的利润，不必知道具体数值，达到即可。

Runtime: 4250 ms, faster than 17.14% of Python3 online submissions for Profitable Schemes.
Memory Usage: 661.3 MB, less than 8.57% of Python3 online submissions for Profitable Schemes.
'''
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(cur_profit, i, member):
            if member > n :
                return 0
            if i >= m:
                return cur_profit == minProfit
            # choose
            c1 = dfs(min(minProfit, cur_profit + profit[i]), i + 1, member + group[i])
            # not choose
            c2 = dfs(cur_profit, i + 1, member)
            return (c1 + c2) % MOD 
            
        return dfs(0, 0, 0)
        
