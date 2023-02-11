'''
BFS

Runtime: 97 ms, faster than 41.94% of Python3 online submissions for Shortest Path with Alternating Colors.
Memory Usage: 14.2 MB, less than 31.23% of Python3 online submissions for Shortest Path with Alternating Colors.
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # graph, 0 for red, 1 for blue
        g = defaultdict(list)
        for a, b in redEdges:
            g[a].append((0, b))
        for a, b in blueEdges:
            g[a].append((1, b))
        # (color, node)
        dist = [[-1] * n for _ in range(2)]
        dist[0][0] = dist[1][0] = 0
        q = deque([(0, 0), (1, 0)])
        while q:
            color, node = q.popleft()
            for ncolor, child in g[node]:
                if color + ncolor == 1 and (dist[ncolor][child] == -1 or dist[color][node] + 1 < dist[ncolor][child]):
                    dist[ncolor][child] = dist[color][node] + 1
                    q.append((ncolor, child))
        
        return [max(dist[0][i], dist[1][i]) if -1 == min(dist[0][i], dist[1][i]) else min(dist[0][i], dist[1][i]) for i in range(n)]
    

'''
BFS, more specific in children-loop for color

Runtime: 91 ms, faster than 65.25% of Python3 online submissions for Shortest Path with Alternating Colors.
Memory Usage: 14.1 MB, less than 73.17% of Python3 online submissions for Shortest Path with Alternating Colors.
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # graph, 0 for red, 1 for blue
        # node -> color(0/1) -> children list
        g = [[[] for _ in range(2)] for _ in range(n)]
        for a, b in redEdges:
            g[a][0].append(b)
        for a, b in blueEdges:
            g[a][1].append(b)
        # (color, node)
        dist = [[-1] * n for _ in range(2)]
        dist[0][0] = dist[1][0] = 0
        q = deque([(0, 0), (1, 0)])
        while q:
            color, node = q.popleft()
            ncolor = 1 - color
            for child in g[node][ncolor]:
                if dist[ncolor][child] == -1 or dist[color][node] + 1 < dist[ncolor][child]:
                    dist[ncolor][child] = dist[color][node] + 1
                    q.append((ncolor, child))
        
        return [max(dist[0][i], dist[1][i]) if -1 == min(dist[0][i], dist[1][i]) else min(dist[0][i], dist[1][i]) for i in range(n)]
    

'''
use Walrus operator

Runtime: 83 ms, faster than 91.50% of Python3 online submissions for Shortest Path with Alternating Colors.
Memory Usage: 14 MB, less than 99.56% of Python3 online submissions for Shortest Path with Alternating Colors.
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # graph, 0 for red, 1 for blue
        # node -> color(0/1) -> children list
        g = [[[] for _ in range(2)] for _ in range(n)]
        for a, b in redEdges:
            g[a][0].append(b)
        for a, b in blueEdges:
            g[a][1].append(b)
        # (color, node)
        dist = [[-1] * n for _ in range(2)]
        dist[0][0] = dist[1][0] = 0
        q = deque([(0, 0), (1, 0)])
        while q:
            color, node = q.popleft()
            ncolor = 1 - color
            for child in g[node][ncolor]:
                if dist[ncolor][child] == -1 or dist[color][node] + 1 < dist[ncolor][child]:
                    dist[ncolor][child] = dist[color][node] + 1
                    q.append((ncolor, child))
        
        ans = []
        for i in range(n):
            if -1 == (min_dist := min(dist[0][i], dist[1][i])):
                ans.append(max(dist[0][i], dist[1][i]))
            else:
                ans.append(min_dist)
        return ans
    
'''
use Walrus operator 2

Runtime: 98 ms, faster than 40.18% of Python3 online submissions for Shortest Path with Alternating Colors.
Memory Usage: 14 MB, less than 97.21% of Python3 online submissions for Shortest Path with Alternating Colors.
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # graph, 0 for red, 1 for blue
        # node -> color(0/1) -> children list
        g = [[[] for _ in range(2)] for _ in range(n)]
        for a, b in redEdges:
            g[a][0].append(b)
        for a, b in blueEdges:
            g[a][1].append(b)
        # (color, node)
        dist = [[-1] * n for _ in range(2)]
        dist[0][0] = dist[1][0] = 0
        q = deque([(0, 0), (1, 0)])
        while q:
            color, node = q.popleft()
            ncolor = 1 - color
            for child in g[node][ncolor]:
                if dist[ncolor][child] == -1 or dist[color][node] + 1 < dist[ncolor][child]:
                    dist[ncolor][child] = dist[color][node] + 1
                    q.append((ncolor, child))
                    
        return [max(dist[0][i], dist[1][i]) if -1 == (min_dist := min(dist[0][i], dist[1][i])) else min_dist for i in range(n)]

