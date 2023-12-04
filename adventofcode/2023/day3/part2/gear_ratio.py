import os 

path = os.path.join(os.path.dirname(__file__), "input")

height = width = 0
scheme = []
with open(path) as f:
    for line in f:
        width = len(line.strip())
        height += 1
        scheme.append(line.strip())

# check symbols, check star(*)
ans = 0
matrix = [[0] * width for _ in range(height)]
for i in range(height):
    for j in range(width):
        ch = scheme[i][j]
        if '*' == ch:
            number_positions =set()
            for ni, nj in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= ni < height and 0 <= nj < width and scheme[ni][nj].isdigit():
                    left, right = nj - 1, nj + 1
                    while left >= 0 and scheme[ni][left].isdigit():
                        left -= 1
                    while right < width and scheme[ni][right].isdigit():
                        right += 1
                    # from left + 1 to right - 1  
                    number_positions.add((ni, left, right))
                    number_positions.add((ni, left, right))
                    
            # only 2 numbers around star
            if 2 == len(number_positions):
                n1_pos, n2_pos = list(number_positions)
                n1 = int(scheme[n1_pos[0]][n1_pos[1] + 1: n1_pos[2]])
                n2 = int(scheme[n2_pos[0]][n2_pos[1] + 1: n2_pos[2]])
                ans += n1 * n2 

print('ans ', ans) # 73074886