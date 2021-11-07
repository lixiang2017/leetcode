'''
DFS

执行用时：3944 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        N = len(values)
        
        # graph
        g = defaultdict(list)
        for u, v, t in edges:
            g[u].append([v, t])
            g[v].append([u, t])

        ans = values[0]
        
        def dfs(node: int, leftTime: int, total_value: int, seen: set):
            nonlocal ans
            if leftTime < 0:
                return
            if node == 0:
                ans = max(ans, total_value)
            
            for child, t in g[node]:
                total = total_value
                if child not in seen:
                    total += values[child]
                dfs(child, leftTime - t, total, seen | {child})
        
        dfs(0, maxTime, values[0], {0})
        return ans

