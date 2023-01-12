'''
DFS

Runtime: 849 ms, faster than 62.82% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.
Memory Usage: 79 MB, less than 5.13% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.
'''
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # graph
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        m = len(edges)
        used_edges = set()
        
        def dfs(node: int, parent: int) -> bool:
            need = False
            for child in g[node]:
                if child != parent:
                    need |= dfs(child, node)
            need |= hasApple[node]
            if need and parent != -1:
                used_edges.add((node, parent))
                used_edges.add((parent, node))
            return need
        
        dfs(0, -1)
        return len(used_edges)
        
