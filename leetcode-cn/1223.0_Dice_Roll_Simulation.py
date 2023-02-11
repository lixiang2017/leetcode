'''
DFS + @cache

执行用时：1660 ms, 在所有 Python3 提交中击败了23.44% 的用户
内存消耗：77.6 MB, 在所有 Python3 提交中击败了37.50% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0:
                return 1
            cnt = 0
            for j, mx in enumerate(rollMax):
                if j != last:
                    cnt += dfs(i - 1, j, mx - 1)
                elif left:
                    cnt += dfs(i - 1, j, left - 1)
            return cnt % MOD
        
        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD

