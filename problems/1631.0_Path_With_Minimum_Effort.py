'''
BFS

Runtime: 4329 ms, faster than 12.26% of Python3 online submissions for Path With Minimum Effort.
Memory Usage: 15.1 MB, less than 93.24% of Python3 online submissions for Path With Minimum Effort.
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, column = len(heights), len(heights[0])
        # position lowest effort
        pos_effort = [[float('inf')] * column for _ in range(row)]
        pos_effort[0][0] = 0
        # when lowest effort update, append it to q 
        # (r, c, min_effort of (max_effort list))
        q = deque([(0, 0, 0)])
        
        dirs = [0, 1, 0, -1, 0]
        while q:
            r, c, _ = q.popleft()
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i + 1]
                if 0 <= nr < row and 0 <= nc < column:
                    from_eff = pos_effort[r][c]
                    to_eff = abs(heights[r][c] - heights[nr][nc]) 
                    min_eff = max(from_eff, to_eff)
                    if pos_effort[nr][nc] > min_eff:
                        pos_effort[nr][nc] = min_eff
                        q.append((nr, nc, min_eff))
                        
        return pos_effort[row - 1][column - 1]

'''
Input
[[1,10,6,7,9,10,4,9]]
Output
5
Expected
9
'''
