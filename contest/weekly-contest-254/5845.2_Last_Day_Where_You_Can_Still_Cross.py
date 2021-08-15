'''
Binary Search + BFS + Memo
Time: O(MN*log(MN))
Space: O(MN)

执行用时：1728 ms, 在所有 Python3 提交中击败了25.00% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
'''
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        N = row * col
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #  all directions, including upward

        def inArea(x, y):
            return 0 <= x < row and 0 <= y < col
        
        def check(idx):
            # matrix
            m = [[0] * col for _ in range(row)]
            for cell in cells[: idx]:
                i, j = cell[0] - 1, cell[1] - 1
                m[i][j] = 1

            q = deque([(0, j) for j in range(col) if m[0][j] == 0])
            # set visited
            m[0][:] = [1] * col
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if inArea(nx, ny) and m[nx][ny] == 0:
                        if nx == row - 1:
                            return True
                        q.append((nx, ny))
                        # set visited!!!! DO NOT FORGET!! otherwise, TLE!!!
                        m[nx][ny] = 1
                
            return False
        
        # binary search
        l, r = 0, N
        ans = 0
        while l <= r:
            mid = l + ((r - l) >> 1)
            if check(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        
        return ans
