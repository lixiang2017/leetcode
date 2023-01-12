'''
DFS

Runtime: 2851 ms, faster than 78.21% of Python3 online submissions for Number of Nodes in the Sub-Tree With the Same Label.
Memory Usage: 230.1 MB, less than 12.18% of Python3 online submissions for Number of Nodes in the Sub-Tree With the Same Label.
'''
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # graph
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        cnt = [[0] * 26 for _ in range(n)]
        
        def dfs(node, parent):
            for child in g[node]:
                if child != parent:
                    child_cnt = dfs(child, node)
                    for i in range(26):
                        cnt[node][i] += child_cnt[i]         
            # self
            idx = ord(labels[node]) - ord('a')
            cnt[node][idx] += 1
            return cnt[node]
        
        dfs(0, -1)
        
        return [cnt[node][ord(labels[node]) - ord('a')] for node in range(n)]
        
