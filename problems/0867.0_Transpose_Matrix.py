'''
Runtime: 102 ms, faster than 45.92% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.7 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
        

'''
Runtime: 96 ms, faster than 52.92% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.8 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        ans = [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j].append(matrix[i][j])
        return ans 
        

'''
Runtime: 99 ms, faster than 50.08% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.8 MB, less than 16.92% of Python3 online submissions for Transpose Matrix.
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        ans = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]
        return ans 
        
        