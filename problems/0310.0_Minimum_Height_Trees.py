'''
Runtime: 386 ms, faster than 18.43% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 19.3 MB, less than 18.13% of Python3 online submissions for Minimum Height Trees.
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        # graph
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        leaves = set(filter(lambda i: len(g[i]) == 1, range(n)))
        
        while len(g) > 2:
            next_leaves = set()
            for leaf in leaves:
                if len(g[leaf]) > 0:
                    center = g[leaf].pop()
                    g[center].discard(leaf)
                    if len(g[center]) <= 1:
                        next_leaves.add(center)  
                g.pop(leaf)
            leaves = next_leaves
        return list(g.keys())
        