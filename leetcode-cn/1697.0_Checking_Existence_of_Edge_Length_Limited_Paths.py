'''
并查集+离线查询
上周赛，灵神讲解了“离线”的含义。
离线：可以不按照询问的顺序，来给出结果。请求的前后顺序没有依赖关系。

上周赛：
https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/
'''
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m = len(queries)
        # union find
        p = list(range(n + 1))
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py

        edgeList.sort(key=lambda e: e[2])
        i, edge_cnt = 0, len(edgeList)
        ans = [False] * m
        for j, query in sorted(enumerate(queries), key=lambda iq_pair: iq_pair[1][2]):
            while i < edge_cnt and edgeList[i][2] < query[2]:
                u, v = edgeList[i][0], edgeList[i][1]
                union(u, v)
                i += 1
            x, y = query[0], query[1]
            if find(x) == find(y):
                ans[j] = True
        return ans 

