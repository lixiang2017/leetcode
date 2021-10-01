'''
DFS

You are here!
Your runtime beats 22.53 % of python3 submissions
You are here!
Your memory usage beats 99.39 % of python3 submissions.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        ans = []
        i = j = 0
        def travel(top, left, bottom, right):
            if top > bottom or left > right:
                return
            # from left to right
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            if top == bottom:
                return
            # from top to bottom
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            if left == right:
                return
            # from right to left
            for j in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom][j])
            # from bottom to top
            for i in range(bottom - 1, top, -1):
                ans.append(matrix[i][left])
            travel(top+1, left+1, bottom-1, right-1)
            
        travel(0, 0, M - 1, N - 1)
        
        return ans
    