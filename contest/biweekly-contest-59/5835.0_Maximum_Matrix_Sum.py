'''
1 日 ago 	Maximum Matrix Sum 	Accepted
'''

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_cnt = 0
        total = 0
        minn = float('inf')
        N = len(matrix)
        
        for i in range(N):
            for j in range(N):
                pos = abs(matrix[i][j])
                minn = min(minn, pos)
                total += pos
                if matrix[i][j] < 0:
                    negative_cnt += 1
                    
        if negative_cnt % 2:
            total -= minn * 2
        
        return total
