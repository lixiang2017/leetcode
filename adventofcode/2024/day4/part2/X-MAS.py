import os 
import re 

ans = 0
matrix = []


with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        line = line.strip()
        matrix.append(line)

row_cnt = len(matrix)
col_cnt = len(matrix[0])


for i in range(1, row_cnt - 1):
    for j in range(1, col_cnt - 1):
        if matrix[i][j] != "A":
            continue
        
        arr = [matrix[i - 1][j - 1], matrix[i - 1][j + 1], matrix[i + 1][j - 1], matrix[i + 1][j + 1]]
        if sorted(arr) == ["M", "M", "S", "S"] and matrix[i - 1][j - 1] != matrix[i + 1][j + 1]:
            ans += 1


print('ans: ', ans) # ans:  1921