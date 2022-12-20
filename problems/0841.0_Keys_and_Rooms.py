'''
BFS + hash set

Runtime: 151 ms, faster than 37.62% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.3 MB, less than 87.64% of Python3 online submissions for Keys and Rooms.
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nxt in rooms[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        return len(seen) == n
