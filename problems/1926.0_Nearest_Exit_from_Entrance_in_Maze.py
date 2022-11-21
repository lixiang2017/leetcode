'''
BFS

Runtime: 2264 ms, faster than 25.35% of Python3 online submissions for Nearest Exit from Entrance in Maze.
Memory Usage: 15.6 MB, less than 26.78% of Python3 online submissions for Nearest Exit from Entrance in Maze.
'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        seen = {tuple(entrance)}
        step = 0
        q = [entrance]
        while q:
            next_q = []
            for x, y in q:
                if [x, y] != entrance and (x in [0, m - 1] or y in [0, n - 1]):
                    return step
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in seen:
                        seen.add((nx, ny))            
                        next_q.append([nx, ny])
            q = next_q
            step += 1
        
        return -1
        