'''
执行用时：604 ms, 在所有 Python3 提交中击败了65.33% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了18.67% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        @cache
        def dfs(left: int, day: int) -> int:
            if day == 1:
                return max(jobDifficulty[left: ])
            cost = inf
            m = 0
            for k in range(left, n - day + 1):
                m = max(m, jobDifficulty[k])
                cost = min(cost, m + dfs(k + 1, day - 1))
            return cost

        return dfs(0, d)
        