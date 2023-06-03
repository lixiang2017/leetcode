'''
DFS

Runtime: 1292 ms, faster than 70.69% of Python3 online submissions for Time Needed to Inform All Employees.
Memory Usage: 53.9 MB, less than 28.83% of Python3 online submissions for Time Needed to Inform All Employees.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)
        ans = 0
        
        def dfs(node, time):
            nonlocal ans
            ans = max(ans, time)
            for child in g[node]:
                dfs(child, time + informTime[node])
                
        dfs(headID, 0)
        return ans


'''
DFS

Runtime: 1326 ms, faster than 59.59% of Python3 online submissions for Time Needed to Inform All Employees.
Memory Usage: 54.1 MB, less than 23.04% of Python3 online submissions for Time Needed to Inform All Employees.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)
        ans = 0
        
        def dfs(node, time):
            nonlocal ans
            ans = max(ans, time)
            for child in g[node]:
                dfs(child, time + informTime[child])
                
        dfs(headID, informTime[headID])
        return ans

'''
BFS

Runtime: 1320 ms, faster than 62.00% of Python3 online submissions for Time Needed to Inform All Employees.
Memory Usage: 44.9 MB, less than 64.05% of Python3 online submissions for Time Needed to Inform All Employees.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)
        ans = 0
        q = deque([(headID, 0)])
        while q:
            node, time = q.popleft()
            ans = max(ans, time)
            for child in g[node]:
                q.append((child, time + informTime[node]))
                
        return ans


'''
BFS

Runtime: 1246 ms, faster than 81.18% of Python3 online submissions for Time Needed to Inform All Employees.
Memory Usage: 46.6 MB, less than 54.28% of Python3 online submissions for Time Needed to Inform All Employees.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)
        ans = 0
        q = deque([(headID, informTime[headID])])
        while q:
            node, time = q.popleft()
            ans = max(ans, time)
            for child in g[node]:
                q.append((child, time + informTime[child]))
                
        return ans


'''
BFS

Runtime: 1223 ms, faster than 85.28% of Python3 online submissions for Time Needed to Inform All Employees.
Memory Usage: 44.8 MB, less than 64.54% of Python3 online submissions for Time Needed to Inform All Employees.
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i, m in enumerate(manager):
            g[m].append(i)
        ans = 0
        q = deque([(headID, informTime[headID])])
        while q:
            node, time = q.popleft()
            ans = max(ans, time)
            for child in g[node]:
                if len(g[child]):
                    q.append((child, time + informTime[child]))
                
        return ans


