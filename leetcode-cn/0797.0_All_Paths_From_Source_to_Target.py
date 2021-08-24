'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了82.56% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了27.34% 的用户
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        N = len(graph)

        def dfs(i, path):
            if i == N - 1:
                ans.append(path)
            for j in graph[i]:
                dfs(j, path + [j])

        dfs(0, [0])
        return ans


'''
BFS

执行用时：40 ms, 在所有 Python3 提交中击败了82.56% 的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了5.17% 的用户
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        N = len(graph)
        # (i, path)
        q = []
        level = [(0, [0])]
        while q != level:
            q = level
            level = []
            for i, path in q:
                for j in graph[i]:
                    if j == N - 1:
                        ans.append(path + [j])
                    level.append((j, path + [j])) 
        return ans