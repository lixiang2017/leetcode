'''
Hash Table + Sort + Union Find
ref:
https://leetcode-cn.com/problems/rank-transform-of-a-matrix/solution/python3-mei-sha-ji-zhu-han-liang-de-ti-jie-by-simp/

You are here!
Your memory usage beats 34.48 % of python3 submissions.
'''
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        LIM = 512
        M, N = len(matrix), len(matrix[0])
        rank = [[0] * N for _ in range(M)]
        # cell value -> position list
        cell2pos = defaultdict(list)
        for i in range(M):
            for j in range(N):
                cell2pos[matrix[i][j]].append([i, j])
            
        # rank for row and column
        rankR, rankC = [0] * M, [0] * N
        
        # union find set
        union = list(range(LIM * 2))  # fatherr
        def find(i):
            if union[i] == i:
                return i
            union[i] = find(union[i])
            return union[i]
    
        # group by row and column
        pool = collections.defaultdict(list)
        # sort by value
        for val in sorted(cell2pos.keys()):
            # union
            for r, c in cell2pos[val]:
                union[find(r)] = find(c + LIM)
            pool.clear()
            for r, c in cell2pos[val]:
                pool[find(r)].append((r, c))
            # elements within same row or same column in a group share one same rank value
            for group in pool.values():
                ra = max(max(rankR[r], rankC[c]) for r, c in group) + 1
                for r, c in group:
                    rankR[r] = rankC[c] = rank[r][c] = ra
                    # reset union find set
                    union[r] = r
                    union[c + LIM] = c + LIM
            
        return rank

'''
[[1,2],[3,4]]
[[7,7],[7,7]]
[[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
[[7,3,6],[1,4,5],[9,8,2]]
[[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]
[[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]

Input:
[[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]
Output:
[[2,1,3,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]]
Expected:
[[2,1,4,6],[2,6,5,4],[5,2,4,3],[4,3,1,5]]    

Input:
[[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]]
Output:
[[3,4,1,2,7],[9,5,3,12,8],[4,6,2,7,5],[7,9,8,1,6],[12,10,4,5,11]]
Expected:
[[3,4,1,2,7],[9,5,3,10,8],[4,6,2,7,5],[7,9,8,1,6],[12,10,4,5,11]]
'''
        
