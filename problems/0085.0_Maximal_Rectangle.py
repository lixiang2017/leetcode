'''
不太懂

Runtime: 224 ms, faster than 54.49% of Python3 online submissions for Maximal Rectangle.
Memory Usage: 16.2 MB, less than 5.42% of Python3 online submissions for Maximal Rectangle.
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        height = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[n] * n for _ in range(m)]
        
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    if i > 0:
                        height[i][j] = height[i-1][j] + 1
                    else:
                        height[i][j] = 1
                    if i > 0:
                        left[i][j] = max(left[i - 1][j], cur_left)
                    else:
                        left[i][j] = cur_left
                else:
                    cur_left = j + 1                
            
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    if i > 0:
                        right[i][j] = min(right[i - 1][j], cur_right)
                    else:
                        right[i][j] = cur_right
                else:
                    right[i][j] = n
                    cur_right = j
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                max_area = max(max_area, (right[i][j] - left[i][j]) * height[i][j])
        
        return max_area
        
