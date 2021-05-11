'''
approach: BFS / Deque
Time: O(N + M), where N is the number of rooms and M is the number of keys.
Time: O(N), where N is the number of rooms.

You are here!
Your runtime beats 97.00 % of python submissions.
You are here!
Your memory usage beats 62.00 % of python submissions.
'''


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        q = collections.deque([0])
        num = 0
        visited = {0}
        
        while q:
            x = q.popleft()
            num += 1
            for key in rooms[x]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        
        return num == N
