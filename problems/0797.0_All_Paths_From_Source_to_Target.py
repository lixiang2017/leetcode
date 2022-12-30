'''
BFS

Runtime: 96 ms, faster than 89.26% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 16 MB, less than 8.23% of Python3 online submissions for All Paths From Source to Target.
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        q = deque([(0, [0])])
        while q:
            node, p = q.popleft()
            if node == n - 1:
                paths.append(p)
            for child in graph[node]:
                q.append((child, p + [child]))
        return paths

'''
DFS

Runtime: 100 ms, faster than 74.93% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 15.5 MB, less than 76.20% of Python3 online submissions for All Paths From Source to Target.
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph)
        
        def backtracking(node, p):
            if node == n - 1:
                paths.append(p)
                return 
            for child in graph[node]:
                backtracking(child, p + [child])
        
        backtracking(0, [0])
        return paths

'''
BFS

Runtime: 113 ms, faster than 70.89% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 15.8 MB, less than 43.50% of Python3 online submissions for All Paths From Source to Target.
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = deque([[0]])
        ans = []
        while paths:
            p = paths.popleft()
            if p[-1] == n - 1:
                ans.append(p)
                continue
            for child in graph[p[-1]]:
                paths.append(p + [child])
        return ans 
