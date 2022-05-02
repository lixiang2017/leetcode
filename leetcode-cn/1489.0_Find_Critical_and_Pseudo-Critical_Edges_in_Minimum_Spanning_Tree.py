'''
多次使用Kruskal算法 （UnionFind）

关键边：这个图的所有可能的最小生成树，共有的边的集合。
如何求解呢：
可以尝试去掉某一条边。如果去掉之后无法连通 或者 去掉之后，可以连通但是代价更大，则这条边是关键边。

伪关键边：在所有可能的最小生成树中出现的边，但不是关键边。
如何求解？同样是尝试每一条边，判断是不是。
在使用并查集求解MST的时候，最先连通这一条边，然后再去处理其他边。
如果最后得到的代价，等于最小代价，则这个边是伪关键边。（但这个边需要先不是关键边）

注意：
因为关键边也满足伪关键边的计算结果验证，所以每次检查某一条边的时候，
如果判断出这条边是关键边后就 continue, 不再判断是否是 伪关键边。

执行用时：1296 ms, 在所有 Python3 提交中击败了44.16% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了64.94% 的用户
通过测试用例：66 / 66
'''
class UnionFind:
    def __init__(self, n) -> None:
        # parents
        self.p = list(range(n))
        # rank, size
        self.rank = [1] * n
        # set count
        self.set_count = n 

    def find(self, x: int) -> int:
        if self.p[x] == x:
            return x 
        root_x = self.find(self.p[x])
        self.p[x] = root_x
        return root_x 

    def union(self, i: int, j: int) -> bool:
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        if self.rank[pi] > self.rank[pj]:
            pi, pj = pj, pi 
        # to make sure, pi <= pj, so pi -> pj
        self.p[pi] = pj 
        self.rank[pj] += self.rank[pi]
        self.set_count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # (from, to, weight, idx) for each edge
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key = lambda e: e[2])
        # min cost for MST, added_cnt
        min_cost = added_cnt = 0
        uf = UnionFind(n)
        for _from, _to, _weight, _idx in edges:
            if uf.union(_from, _to):
                min_cost += _weight 
                added_cnt += 1
                if added_cnt == n - 1:
                    break 
        
        ans = [list(), list()]
        m = len(edges)
        # check every edge
        for i in range(m):
            # check edges[i] is critical or not, remove/ignore edges[i]
            cost = 0
            uf = UnionFind(n)
            for j, (_from, _to, _weight, _idx) in enumerate(edges):
                if i != j and uf.union(_from, _to):
                    cost += _weight
            # if uf.set_count != 1 or (uf.set_count == 1 and cost > min_cost):  # also ok 
            if uf.set_count != 1 or cost > min_cost:
                edge_idx = edges[i][3]
                ans[0].append(edge_idx)
                continue

            # check edges[i] is pseudo-critical or not 
            uf = UnionFind(n)
            # add edges[i] first
            _from, _to, _weight, _idx = edges[i]
            uf.union(_from, _to)
            cost = _weight
            for j, (_from, _to, _weight, _idx) in enumerate(edges):
                if i != j and uf.union(_from, _to):
                    cost += _weight
            if cost == min_cost:
                edge_idx = edges[i][3]
                ans[1].append(edge_idx)

        return ans 


'''
输入：
6
[[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]
输出：
[[6],[0,1,2,3,4,5]]
预期结果：
[[3],[0,1,2,4,5,6]]
'''


