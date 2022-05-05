'''
prim

执行用时：1096 ms, 在所有 Python3 提交中击败了83.68% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        start = random.randrange(0, n)
        return self.prim(points, start)

    def prim(self, points, start) -> int:
        n = len(points)
        # manhattan distance
        dist = lambda i, j: abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        cost = 0
        low_cost = [float('inf')] * n
        # added to MST
        added = [False] * n 
        added_cnt = 0
        # start
        low_cost[start] = 0
        while added_cnt < n:
            # find lowest_cost node min_idx, add it to MST
            # suppose 0
            min_idx = None 
            min_cost = float('inf')
            for k in range(n):
                if (not added[k]) and low_cost[k] < min_cost:
                    min_idx = k
                    min_cost = low_cost[k]
            cost += low_cost[min_idx]
            added[min_idx] = True
            added_cnt += 1
            # update low_cost, from j to other nodes
            for k in range(n):
                weight = dist(min_idx, k)
                if (not added[k]) and weight < low_cost[k]:
                    low_cost[k] = weight

        return cost


'''
prim + pq

执行用时：528 ms, 在所有 Python3 提交中击败了99.70% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了92.22% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        start = random.randrange(0, n)
        return self.prim(points, start)

    def prim(self, points, start) -> int:
        n = len(points)
        # manhattan distance
        dist = lambda i, j: abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        cost = 0
        low_cost = [float('inf')] * n
        # added to MST
        added_cnt = 0
        not_added = set(range(n))
        # start
        low_cost[start] = 0
        # pq, (dist, idx)
        h = []
        heappush(h, (0, start))

        while h:
            # find lowest_cost node min_idx, add it to MST
            min_cost, min_idx  = heappop(h)
            if min_idx not in not_added:
                continue
            cost += min_cost
            not_added.remove(min_idx)
            added_cnt += 1
            if added_cnt == n:
                break
            # update low_cost, from j to other nodes
            for k in not_added:
                weight = dist(min_idx, k)
                if weight < low_cost[k]:
                    low_cost[k] = weight
                    heappush(h, (weight, k))

        return cost



'''
kruskal (UnionFind)

执行用时：1344 ms, 在所有 Python3 提交中击败了63.77% 的用户
内存消耗：81.1 MB, 在所有 Python3 提交中击败了76.35% 的用户
通过测试用例：72 / 72
'''
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        self.set_count = n 

    def find(self, x):
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # make sure size_px <= size_py, so px -> py
        if self.size[px] > self.size[py]:
            px, py = py, px 
        self.p[px] = py 
        self.size[py] += self.size[px]
        self.set_count -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal
        dist = lambda i, j: abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))

        uf = UnionFind(n)

        # sort by length of edges
        edges.sort()
        cost = link_cnt = 0
        for dist, i, j in edges:
            if uf.union(i, j):
                cost += dist 
                link_cnt += 1
                if link_cnt == n - 1:
                    break 
        return cost 




