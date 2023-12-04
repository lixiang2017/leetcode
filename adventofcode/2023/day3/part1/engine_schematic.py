import os 

path = os.path.join(os.path.dirname(__file__), "input")

height = width = 0
scheme = []
with open(path) as f:
    for line in f:
        width = len(line.strip())
        height += 1
        scheme.append(line.strip())

# check symbols
matrix = [[0] * width for _ in range(height)]
for i in range(height):
    for j in range(width):
        ch = scheme[i][j]
        if not ch.isdigit() and ch != '.':
            for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= ni < height and 0 <= nj < width and scheme[ni][nj].isdigit():
                    matrix[ni][nj] = 1
                    
                    
# extend for numbers
ans = 0
for i, row in enumerate(matrix):
    right = -1
    for j, x in enumerate(row):
        if j <= right - 1:
            continue
        if 1 == x:
            left, right = j - 1, j + 1
            while left >= 0 and scheme[i][left].isdigit():
                left -= 1
            while right < width and scheme[i][right].isdigit():
                right += 1
            # from left + 1 to right - 1  
            ans += int(scheme[i][left + 1: right])
            
print('ans ', ans) # 4361  # 527369