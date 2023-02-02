'''
BFS

执行用时：36 ms, 在所有 Python3 提交中击败了96.27% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了62.73% 的用户
通过测试用例：90 / 90
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in redEdges:
            g[a].append([b, 0])
        for u, v in blueEdges:
            g[u].append([v, 1])
        # distance, 0 for r, 1 for b
        dist = [[0, 0]] + [[-1, -1] for _ in range(n - 1)]
        # start from 0-th node, 0 for r, 1 for b
        q = deque([(0, 0), (0, 1)])
        while q:
            node, color = q.popleft()
            for child, cur_color in g[node]:
                if color + cur_color == 1 and (dist[child][cur_color] == -1 or dist[node][color] + 1 < dist[child][cur_color]):
                    dist[child][cur_color] = dist[node][color] + 1
                    q.append((child, cur_color))
        return [min(dist[i]) if -1 not in dist[i] else max(dist[i]) for i in range(n)]
