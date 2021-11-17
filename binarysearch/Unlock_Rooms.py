'''
BFS
T: O(N)
S: O(N)

Success!
Your code took 3 milliseconds — faster than 99.01% in Python
'''
class Solution:
    def solve(self, rooms):
        N = len(rooms)
        seen = set([0])
        q = deque([0])

        while q:
            r0 = q.popleft()
            for r in rooms[r0]:
                if r not in seen:
                    q.append(r)
                    seen.add(r)
                    
        return len(seen) == N


'''
DFS
T: O(N)
S: O(N)

Success!
Your code took 6 milliseconds — faster than 51.35% in Python
'''
class Solution:
    def solve(self, rooms):
        N = len(rooms)
        seen = set()
        
        def dfs(r):
            if r in seen:
                return
            seen.add(r)
            for rr in rooms[r]:
                dfs(rr)

        dfs(0)
        return len(seen) == N
