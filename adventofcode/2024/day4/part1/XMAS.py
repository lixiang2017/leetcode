import os 
import re 

ans = 0
matrix = []
pat1 = r"XMAS"
pat2 = r"SAMX"


with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        line = line.strip()
        matrix.append(line)
        m1 = re.findall(pat1, line)
        m2 = re.findall(pat2, line)
        ans += len(m1) + len(m2)
        # print("*" * 100)
        print(m1)
        print(m2)

row_cnt = len(matrix)
col_cnt = len(matrix[0])


for i in range(row_cnt):
    for j in range(col_cnt):
        # down 
        if i + 3 < row_cnt:
            if (matrix[i][j] == "X" and matrix[i + 1][j] == "M" and matrix[i + 2][j] == "A" and matrix[i + 3][j] == "S") or (matrix[i][j] == "S" and matrix[i + 1][j] == "A" and matrix[i + 2][j] == "M" and matrix[i + 3][j] == "X"):
                ans += 1
        # left down
        if i + 3 < row_cnt and j - 3 >= 0:
            if (matrix[i][j] == "X" and matrix[i + 1][j - 1] == "M" and matrix[i + 2][j - 2] == "A" and matrix[i + 3][j - 3] == "S") or (matrix[i][j] == "S" and matrix[i + 1][j - 1] == "A" and matrix[i + 2][j - 2] == "M" and matrix[i + 3][j - 3] == "X"):
                ans += 1
        # right down
        if i + 3 < row_cnt and j + 3 < col_cnt:
            if (matrix[i][j] == "X" and matrix[i + 1][j + 1] == "M" and matrix[i + 2][j + 2] == "A" and matrix[i + 3][j + 3] == "S") or (matrix[i][j] == "S" and matrix[i + 1][j + 1] == "A" and matrix[i + 2][j + 2] == "M" and matrix[i + 3][j + 3] == "X"):
                ans += 1

print('ans: ', ans) # 