'''
Time: O(2N)
Space: O(2N)

You are here!
Your runtime beats 65.98 % of python3 submissions.
You are here!
Your memory usage beats 62.07 % of python3 submissions.
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        reshape = []
        one_line = []
        for row in mat:
            one_line.extend(row)
        i = 0
        while i < m * n:
            reshape.append(one_line[i: i + c])
            i += c
        return reshape

'''
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 94.94 % of python3 submissions.
You are here!
Your memory usage beats 99.66 % of python3 submissions.
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
                    
        it = iter(item for row in mat for item in row)
        reshape = []
        for _ in range(r):
            one_line = []
            for _ in range(c):
                one_line.append(next(it))
            reshape.append(one_line)
        return reshape

'''
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 41.38 % of python3 submissions.
You are here!
Your memory usage beats 62.07 % of python3 submissions.
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
                    
        reshape = [[0] * c for _ in range(r)]
        for k, value in enumerate(chain(*mat)):
            i, j = divmod(k, c)
            reshape[i][j] = value
        return reshape


'''
You are here!
Your runtime beats 84.71 % of python3 submissions.
You are here!
Your memory usage beats 20.69 % of python3 submissions.
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
                    
        reshape = [[0] * c for _ in range(r)]
        for h in range(m):
            IDX = h * n
            for w in range(n):
                idx = IDX + w
                i, j = divmod(idx, c)
                reshape[i][j] = mat[h][w]
        return reshape
                

'''
You are here!
Your runtime beats 65.98 % of python3 submissions.
You are here!
Your memory usage beats 41.26 % of python3 submissions.
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
                    
        one = [element for row in mat for element in row]
        return [one[i * c: (i + 1) * c] for i in range(r)]
                







             