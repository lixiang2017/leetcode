'''
Dijkstra + heapq
稀疏图用堆

执行用时：172 ms, 在所有 Python3 提交中击败了82.76% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了95.02% 的用户
通过测试用例：16 / 16
'''
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # graph
        g = defaultdict(dict)
        for e, p in zip(edges, succProb):
            a, b = e
            g[a][b] = p
            g[b][a] = p

        prob = [0] * n
        prob[start] = 1
        # heap (-p, node)
        h = [(-1, start)]
        while h:
            neg_p, node = heappop(h)
            node_p = -neg_p
            for child, p in g[node].items():
                if node_p * p > prob[child]:
                    prob[child] = node_p * p
                    heappush(h, (-prob[child], child))
        return prob[end]                

