'''
DFS + memoization

Runtime: 1682 ms, faster than 87.22% of Python3 online submissions for Count All Possible Routes.
Memory Usage: 22.1 MB, less than 60.90% of Python3 online submissions for Count All Possible Routes.
'''
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)
        
        @cache
        def dfs(i, left):
            if left < 0:
                return 0
            count = 0
            if i == finish:
                count += 1
            for j in range(n):
                need = abs(locations[i] - locations[j])
                if j != i and need <= left:
                    count += dfs(j, left - need)
            return count % MOD
        
        return dfs(start, fuel)
