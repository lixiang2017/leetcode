'''
graph

执行用时：96 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了24.65% 的用户
通过测试用例：82 / 82
'''
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # graph
        g = defaultdict(set)
        for a, b in roads:
            g[a].add(b)
            g[b].add(a)
        ans = 0
        for a in g:
            for b in g:
                if a != b:
                    rank = len(g[a]) + len(g[b]) - int(a in g[b])
                    if rank > ans:
                        ans = rank
        return ans 

