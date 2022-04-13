'''
T: O(M*N)
S: O(M*N)

Runtime: 187 ms, faster than 76.60% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.3 MB, less than 35.10% of Python3 online submissions for Shift 2D Grid.
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) if grid else 0
        k %= (m * n)
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                idx = i * n + j
                ni, nj = divmod((idx + k) % (m * n), n)
                ans[ni][nj] = x
            
        return ans 
    


'''
T: O(2 * M * N)
S: O(1)

Runtime: 200 ms, faster than 68.24% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.3 MB, less than 35.10% of Python3 online submissions for Shift 2D Grid.
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) if grid else 0
        k %= (m * n)
        
        def reverse(start, end):
            while start < end:
                li, lj = divmod(start, n)
                ri, rj = divmod(end, n)
                grid[li][lj], grid[ri][rj] = grid[ri][rj], grid[li][lj]
                start += 1
                end -= 1
        
        reverse(0, m * n - 1)
        reverse(0, k - 1)
        reverse(k, m * n - 1)
        return grid 


'''
Runtime: 255 ms, faster than 45.68% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 14.3 MB, less than 35.10% of Python3 online submissions for Shift 2D Grid.
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) if grid else 0
        k %= (m * n)
        start = m * n - k
        
        ans = []
        for i in range(start, start + m * n):
            i %= (m * n)
            r, c = divmod(i, n)
            if (i - start) % n == 0:
                ans.append([])
            ans[-1].append(grid[r][c])

        return ans



