'''
提前判断
if n >= d
if n * (n + 1) // 2 < d
提前退出搜索
if can_win:

执行用时：3556 ms, 在所有 Python3 提交中击败了18.68% 的用户
内存消耗：239.7 MB, 在所有 Python3 提交中击败了5.12% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        n, d = maxChoosableInteger, desiredTotal 
        if n >= d:
            return True 
        if n * (n + 1) // 2 < d:
            return False 

        @lru_cache(None)
        def dfs(mask, cur_sum) -> bool:
            can_win = False
            for i in range(n, 0, -1):
                if 0 == (mask >> i & 1):
                    if cur_sum + i >= d:
                        return True 
                    can_win |= (not dfs(mask | (1 << i) , cur_sum + i))
                    if can_win:
                        return True 
            return can_win
        
        return dfs(0, 0)
