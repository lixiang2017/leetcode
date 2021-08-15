'''
3 / 117 个通过测试用例
状态：超出时间限制
提交时间：3 小时前
最后执行的输入：
6
2
[[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]]


Binary Search + BFS
'''
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        N = row * col
        states = []
        state = [[0] * col for _ in range(row)]
        
        states.append(deepcopy(state))
        for i, cell in enumerate(cells):
            r, c = cell[0] - 1, cell[1] - 1
            state[r][c] = 1
            states.append(deepcopy(state))
        
        #print(states)
        dirs = [(1, 0), (0, -1), (0, 1)]  #  (-1, 0), 
        def inArea(x, y):
            return 0 <= x < row and 0 <= y < col
        
        def check(idx):
            # matrix
            m = states[idx]
            q = deque([(0, j) for j in range(col) if m[0][j] == 0])
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if inArea(nx, ny) and m[nx][ny] == 0:
                        if nx == row - 1:
                            return True
                        q.append((nx, ny))
                
            return False
        
        # binary search
        l, r = 0, N
        ans = 0
        while l <= r:
            mid = l + ((r - l) >> 1)
            if check(mid):
                #print('check: ', mid)
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        
        return ans

