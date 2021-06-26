'''
approach: BFS + Hash Set

执行用时：180 ms, 在所有 Python3 提交中击败了5.67% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.67% 的用户
'''

import copy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [[1,2,3],[4,5,0]]
        if board == target:
            return 0
        
        # (x, y) for 0 position
        x = y = 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j
        
        def get(status, x, y):
            # next_status = status[:]  # wrong
            # next_status = copy.deepcopy(status)   # wrong
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for deltax, deltay in directions:
                nx, ny = x + deltax, y + deltay
                if 0 <= nx < 2 and 0 <= ny < 3:
                    next_status = copy.deepcopy(status)
                    next_status[x][y], next_status[nx][ny] = next_status[nx][ny], next_status[x][y]
                    yield (next_status, nx, ny)

        seen = {tuple(board[0] + board[1])}
        q = deque([(board, 0, x, y)])   # (board, step, x, y)
        while q:
            status, step, x, y = q.popleft()
            for next_status, xn, yn in get(status, x, y):
                if tuple(next_status[0] + next_status[1]) not in seen:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1, xn, yn))
                    seen.add(tuple(next_status[0] + next_status[1]))

        return -1

