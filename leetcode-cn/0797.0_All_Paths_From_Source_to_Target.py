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
BFS. use two lists, not use deque.

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


'''
DFS + yield (from)

执行用时：44 ms, 在所有 Python3 提交中击败了66.49% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了86.87% 的用户
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        def dfs(node: int, path: List[int]):
            if node == N - 1:
                yield path
            for child in graph[node]:
                yield from dfs(child, path + [child])
                
        return list(dfs(0, [0]))


'''
DFS
return [item for item in dfs(0, [0])] 更快一些

执行用时：36 ms, 在所有 Python3 提交中击败了92.23% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了43.17% 的用户
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        def dfs(node: int, path: List[int]):
            if node == N - 1:
                yield path
            for child in graph[node]:
                yield from dfs(child, path + [child])

        return [item for item in dfs(0, [0])]


'''
BFS, use deque

执行用时：36 ms, 在所有 Python3 提交中击败了92.23% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了31.09% 的用户
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        q = deque([(0, [0])])
        ans = []
        while q:
            node, path = q.popleft()
            if node == N - 1:
                ans.append(path)
            for child in graph[node]:
                q.append((child, path + [child]))
        return ans










