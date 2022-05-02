'''
Kruskal + UnionFind + Sort + Minimum Spanning Tree + Greedy

T: O(N^2 + N^2*log(N^2) + N^2*alpha(N)) = O(N^2 * logN)
S: O(N + N + N^2) = O(N^2)

Kruskal算法可以解决的问题：
将一个完全连通的图，化简成一个最小生成树。可以算出这个最小生成树的所有边之和，也即代价。

Kruskal算法思想：
先将所有 [边] 按照 长度/代价，从小到大排序。依次选择加入最小生成树。
如果选择之后，不会构成环，则可以选择这条边加入最小生成树。否则，放弃这条边。
判断是否构成环，采用并查集，如果两个点不在同一个联通分量里，即可加入。

这个算法为什么是正确的？即为什么排序之后按照排序处理是正确的？

Runtime: 2696 ms, faster than 51.17% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 96.9 MB, less than 48.59% of Python3 online submissions for Min Cost to Connect All Points.
'''
class UnionFind:
    def __init__(self, n):
        # n nodes
        self.parents = list(range(n))
        # rank, the number of children for every node
        self.rank = [1] * n
    
    def find(self, i):
        x = i
        while self.parents[x] != x:
            x = self.parents[x]
        # point to x directly, path compression
        while self.parents[i] != x:
            pi = self.parents[i]
            self.parents[i] = x
            i = pi
        return x 
    
    def union(self, i, j):
        # root of i, j
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            if self.rank[ri] < self.rank[rj]:
                self.parents[ri] = rj 
                self.rank[rj] += self.rank[rj]
            else:
                self.parents[rj] = ri
                self.rank[ri] += self.rank[rj]
            return True
        else:
            return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # (dist, point1_idx, point2_idx)
        edges = []
        
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # manhanttan distance
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append([dist, i, j])    
                
        uf = UnionFind(n)
        edges.sort()
        ans = span_cnt = 0
        for dist, i, j in edges:
            if uf.union(i, j):
                ans += dist
                span_cnt += 1
            if span_cnt == n - 1:
                break 
                
        return ans 
                


'''
find 里压缩路径的写法要注意下

Runtime: 3611 ms, faster than 34.78% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 96.9 MB, less than 48.59% of Python3 online submissions for Min Cost to Connect All Points.
'''
class UnionFind:
    def __init__(self, n):
        # n nodes
        self.parents = list(range(n))
        # rank, the number of children for every node
        self.rank = [1] * n
    
    def find(self, i):
        if self.parents[i] == i:
            return i 
        root_i = self.find(self.parents[i])
        self.parents[i] = root_i 
        return root_i 

    def union(self, i, j):
        # root of i, j
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return False
        
        if self.rank[ri] > self.rank[rj]:
            ri, rj = rj ,ri
        self.parents[ri] = rj 
        self.rank[rj] += self.rank[rj]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda i, j: abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        n = len(points)
        # (dist, point1_idx, point2_idx)
        edges = []
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # manhanttan distance
                edges.append([dist(i, j), i, j])    
                
        uf = UnionFind(n)
        edges.sort()
        ans = span_cnt = 0
        for dist, i, j in edges:
            if uf.union(i, j):
                ans += dist
                span_cnt += 1
            if span_cnt == n - 1:
                break 
                
        return ans 
                

'''
prim

MST: Minimum Spanning Tree
prim算法以 [顶点] 为考虑因素。计算过程中会把所有点划分成两部分，[加入MST的点的集合] 和 [未加入MST的点的集合] 
初始，可以选择随机选择一个点放入 MST，同时更新其他所有点到这个初始点的最小代价low_cost.
接下来，迭代 N-1次，每次从 [未加入MST的点的集合] 选择一个low_cost最小的点，放入 [MST的点的集合].
同时，其他未加入的点 可能会因为这个加入的点，low_cost值发生变化。
所以，要根据这个新加入的点，更新其他未加入的点的low_cost值。

T: O(N^2)
S: O(N^2)

Runtime: 2513 ms, faster than 54.87% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 37.2 MB, less than 92.24% of Python3 online submissions for Min Cost to Connect All Points.
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        start = random.randint(0, n - 1)
        # start = random.randrange(0, n)
        return self.prim(points, start)
    
    def prim(self, points: List[List[int]], start: int) -> int:
        n = len(points)
        # graph, distance from i to j 
        g = [[float('inf')] * n for _ in range(n)]
        for i in range(n - 1):
            for j in range(n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                g[i][j] = dist
                g[j][i] = dist
        
        cost = 0  # answer
        # every not-added node, lowest cost to Minimum Spanning Tree(added nodes)
        low_cost = [float('inf')] * n 
        # added nodes to MST 
        added = [False] * n
        
        # start
        added[start] = True
        for i in range(n):
            if i == start: continue
            low_cost[i] = g[i][start]
        
        # left n-1 nodes, need to add to MST
        for _ in range(n - 1):
            # find min cost index 
            min_idx = 0
            min_cost = float('inf')
            for j in range(n):
                if not added[j] and low_cost[j] < min_cost:
                    min_cost = low_cost[j]
                    min_idx = j
                    
            # add to MST
            cost += min_cost 
            added[min_idx] = True
            # update low_cost 
            for j in range(n):
                if not added[j] and g[j][min_idx] < low_cost[j]:
                    low_cost[j] = g[j][min_idx]
            
        return cost 
    
    
    
    
'''
prim
使用 Hash Set 表示哪些节点未加入 MST

Runtime: 2015 ms, faster than 66.88% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 37.5 MB, less than 92.20% of Python3 online submissions for Min Cost to Connect All Points.
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # start = random.randint(0, n - 1)
        start = random.randrange(0, n)
        return self.prim(points, start)
    
    def prim(self, points: List[List[int]], start: int) -> int:
        n = len(points)
        # graph, distance from i to j 
        g = [[float('inf')] * n for _ in range(n)]
        for i in range(n - 1):
            for j in range(n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                g[i][j] = dist
                g[j][i] = dist
        
        cost = 0  # answer
        # every not-added node, lowest cost to Minimum Spanning Tree(added nodes)
        low_cost = [float('inf')] * n 
        # not added nodes set, not added nodes to MST 
        not_added = set(range(n))
        
        # start
        not_added.remove(start)
        for i in range(n):
            if i == start: continue
            low_cost[i] = g[i][start]    
        
        # left n-1 nodes, need to add to MST
        for _ in range(n - 1):
            # find min cost index 
            min_idx = 0
            min_cost = float('inf')
            for j in not_added:
                if low_cost[j] < min_cost:
                    min_cost = low_cost[j]
                    min_idx = j
                    
            # add to MST
            cost += min_cost 
            not_added.remove(min_idx)
            # update low_cost 
            for j in not_added:
                if g[j][min_idx] < low_cost[j]:
                    low_cost[j] = g[j][min_idx]
            
        return cost 
    
    
    

    

'''
prim
使用 Hash Set 表示哪些节点未加入 MST
使用优先队列优化每次选择
使用邻接表，记录每个节点的邻居列表。对于稀疏图，可大大降低图的复杂度。
这里没有使用 low_cost 数组

Runtime: 2015 ms, faster than 66.88% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 106.9 MB, less than 42.67% of Python3 online submissions for Min Cost to Connect All Points.
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # start = random.randint(0, n - 1)
        start = random.randrange(0, n)
        return self.prim(points, start)
    
    def prim(self, points: List[List[int]], start: int) -> int:
        n = len(points)
        # graph, i -> nodes list
        g = defaultdict(list)
        for i in range(n - 1):
            for j in range(n):
                g[i].append(j)
                g[j].append(i)
        
        cost = 0  # answer
        # added nodes to MST
        added = [False] * n
        # not added nodes set, not added nodes to MST 
        not_added = set(range(n))
        
        # priority queue, (distance, node_idx)
        h = []
        heappush(h, (0, start))
        
        # left n-1 nodes, need to add to MST
        while h:
            dist, idx = heappop(h)
            if added[idx]:
                continue
            # add node_idx 
            cost += dist 
            added[idx] = True
            not_added.remove(idx)
            if not not_added:
                return cost
            for j in not_added:
                weight = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                heappush(h, (weight, j))
        
        return cost 
    
    

'''
prim
使用 Hash Set 表示哪些节点未加入 MST
使用优先队列优化每次选择
使用邻接表，记录每个节点的邻居列表。对于稀疏图，可大大降低图的复杂度。
同时使用 low_cost 数组，把变小的 low_cost 再加入优先队列。降低优先队列的规模。

Runtime: 1149 ms, faster than 93.10% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 57.3 MB, less than 91.86% of Python3 online submissions for Min Cost to Connect All Points.
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # start = random.randint(0, n - 1)
        start = random.randrange(0, n)
        return self.prim(points, start)
    
    def prim(self, points: List[List[int]], start: int) -> int:
        n = len(points)
        # graph, i -> nodes list
        g = defaultdict(list)
        for i in range(n - 1):
            for j in range(n):
                g[i].append(j)
                g[j].append(i)
        
        cost = 0  # answer
        # every not-added node, lowest cost to Minimum Spanning Tree(added nodes)
        low_cost = [float('inf')] * n 
        # not added nodes set, not added nodes to MST 
        not_added = set(range(n))
        
        # priority queue, (distance, node_idx)
        h = []
        heappush(h, (0, start))
        
        # left n-1 nodes, need to add to MST
        while h:
            dist, idx = heappop(h)
            if idx not in not_added:
                continue
            # add node_idx 
            cost += dist 
            not_added.remove(idx)
            if not not_added:
                return cost
            for j in not_added:
                weight = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                if weight < low_cost[j]:
                    low_cost[j] = weight
                    heappush(h, (weight, j))
        
        return cost 
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    


    
    


    
    




