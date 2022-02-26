'''
思路：
1、shortest path -> 最短路径 -> BFS
2、可以从每个节点开始 -> 多源BFS
3、访问所有节点时的状态为 (1 << n) - 1  -> 状态压缩

T: O(N^2 * 2^N)
S: O(N * 2^N)
Runtime: 322 ms, faster than 57.29% of Python3 online submissions for Shortest Path Visiting All Nodes.
Memory Usage: 18.9 MB, less than 58.49% of Python3 online submissions for Shortest Path Visiting All Nodes.
'''
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # (curr_node, state, step)
        q = deque([(i, 1 << i, 0) for i in range(n)])
        # (curr_node, state)
        seen = {(i, 1 << i) for i in range(n)}
        
        while q:
            node, state, step = q.popleft()
            if state == (1 << n) - 1:
                return step
            # neighbor
            for v in graph[node]:
                nxt_state = state | (1 << v)
                if (v, nxt_state) not in seen:
                    seen.add((v, nxt_state))
                    q.append((v, nxt_state, step + 1))
        
        return -1
