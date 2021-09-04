'''
217 / 217 个通过测试用例
状态：通过
执行用时: 464 ms
内存消耗: 127.8 MB
提交时间：1 小时前
'''
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        M, N = len(land), len(land[0])
        
        def dfs(i, j):
            r1 = r2 = i
            c1 = c2 = j
            land[i][j] = -1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    if land[ni][nj] == 1:
                        r2 = max(r2, ni)
                        c2 = max(c2, nj)
                        _, _, nr2, nc2 = dfs(ni, nj)
                        r2 = max(r2, nr2)
                        c2 = max(c2, nc2)
            return [r1, c1, r2, c2]
        
        for i in range(M):
            for j in range(N):
                if land[i][j] == 1:
                    ans.append(dfs(i, j))

        return ans