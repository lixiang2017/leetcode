'''
hash table + prefix sum

Runtime: 1888 ms, faster than 15.64% of Python3 online submissions for Number of Submatrices That Sum to Target.
Memory Usage: 14.8 MB, less than 93.84% of Python3 online submissions for Number of Submatrices That Sum to Target.
'''

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0]) if matrix else 0 
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + x 
        
        for r1 in range(m):
            for r2 in range(r1, m):
                d = Counter({0: 1})
                cur = 0
                for c in range(n):
                    cur = pre[r2 + 1][c + 1] - pre[r1][c + 1]
                    ans += d[cur - target]     
                    d[cur] += 1                
        return ans 
