'''
DFS + 三色标记法
Time: O(V + E)
Space: O(V)

执行用时：112 ms, 在所有 Python3 提交中击败了91.33% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了53.18% 的用户
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        '''
        0: not visited
        1: visited, in stack
        2: safe
        '''
        state = [0] * N

        def safe(i):
            if state[i] > 0:
                return state[i] == 2
            state[i] = 1
            for y in graph[i]:
                if not safe(y):
                    return False
            state[i] = 2
            return True
        
        return [i for i in range(N) if safe(i)]


'''
Reversed Graph + Topological Sort

执行用时：164 ms, 在所有 Python3 提交中击败了56.07% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了67.05% 的用户
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # reversed graph
        N = len(graph)
        rg = [[] for _ in range(N)]
        # init rg
        for u, vs in enumerate(graph):
            for v in vs:
                rg[v].append(u)
        # in_deg in rg, 反图的入度的是原图的出度
        in_deg = [len(vs) for vs in graph]
        q = deque([i for i, d in enumerate(in_deg) if 0 == d])
        while q:
            x = q.popleft()
            for y in rg[x]:
                in_deg[y] -= 1
                if 0 == in_deg[y]:
                    q.append(y)
        
        return [i for i, d in enumerate(in_deg) if 0 == d]
