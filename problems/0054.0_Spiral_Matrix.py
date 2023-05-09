'''
Runtime: 49 ms, faster than 6.74% of Python3 online submissions for Spiral Matrix.
Memory Usage: 16.5 MB, less than 6.05% of Python3 online submissions for Spiral Matrix.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            # from left to right
            ans.extend(matrix[top][left: right + 1])
            if top == bottom:
                break
            # from top to bottom
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])
            if left == right:
                break
            # from right to left
            ans.extend(matrix[bottom][left: right][:: -1])
            # from bottom to top
            for i in range(bottom - 1, top, -1):
                ans.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        
        return ans 
        