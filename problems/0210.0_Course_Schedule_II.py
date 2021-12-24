'''
BFS

Runtime: 100 ms, faster than 66.08% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.6 MB, less than 67.31% of Python3 online submissions for Course Schedule II.
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a, b]   b -> a
        indegree = [0] * numCourses
        out = defaultdict(set)
        for a, b in prerequisites:
            out[b].add(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for child in out[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    
        return [[], ans][len(ans) == numCourses]
        
