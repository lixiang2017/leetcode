'''
Hash Table + DFS
连通块标记 

ref:
https://leetcode-cn.com/problems/making-a-large-island/solution/827zui-da-ren-gong-dao-python3-shi-yong-wwkd5/

You are here!
Your runtime beats 89.27 % of python3 submissions.
You are here!
Your memory usage beats 74.00 % of python3 submissions.
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        # island index from 2
        islandIdx = 2
        # idxIsland -> size
        markIsland = dict()
        
        def inArea(i, j):
            return 0 <= i < M and 0 <= j < N
        
        def area_size(islandIdx, i, j):
            if not inArea(i, j):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = islandIdx
            return 1 + area_size(islandIdx, i - 1, j) + area_size(islandIdx, i + 1, j) \
                + area_size(islandIdx, i, j - 1) + area_size(islandIdx, i, j + 1)
    
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    markIsland[islandIdx] = area_size(islandIdx, i, j)
                    islandIdx += 1
        
        # all 0s
        if len(markIsland) == 0:
            return 1
        # all 1s
        if max(markIsland.values()) == M * N:
            return M * N
        
        def idx_size(i, j):
            if not inArea(i, j):
                return 0, 0
            if 0 == grid[i][j]:
                return 0, 0
            return grid[i][j], markIsland[grid[i][j]]
        
        def neighbor_size(i, j):
            DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))
            area = dict()
            for dr, dc in DIR:
                ni, nj = i + dr, j + dc
                idx, size = idx_size(ni, nj)
                if idx not in area:
                    area[idx] = size
        
            return sum(area.values())
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if 0 == grid[i][j]:
                    size = 1 + neighbor_size(i, j)
                    ans = max(ans, size)
        return ans

