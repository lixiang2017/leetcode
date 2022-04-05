'''
执行用时：132 ms, 在所有 Python3 提交中击败了81.26% 的用户
内存消耗：28.9 MB, 在所有 Python3 提交中击败了5.16% 的用户
通过测试用例：71 / 71
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
            
        nodes = set(range(n))
        g = defaultdict(set)
        # cut edges/branches, from leaves to root
        q = deque()

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        for i in range(n):
            if 1 == len(g[i]):
                q.append(i)
                nodes.remove(i)
            
        while len(nodes) > 2:
            for _ in range(len(q)):
                node = q.popleft()
                neigh = g[node].pop()
                g[neigh].remove(node)
                if 1 == len(g[neigh]):
                    q.append(neigh)
                    nodes.remove(neigh)
        
        return list(nodes)
        