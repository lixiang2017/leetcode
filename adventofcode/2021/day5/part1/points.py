

max_x = max_y = 0

with open('input') as f:
    for line in f:
        x1y1, x2y2 = line.split('->')
        x1, y1 = x1y1.strip().split(',')
        x2, y2 = x2y2.strip().split(',')
        x1, y1, x2, y2 = x1.strip(), y1.strip(), x2.strip(), y2.strip()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        max_x, max_y = max(max_x, x1, x2), max(max_y, y1, y2)

print('max_x: ', max_x, 'max_y: ', max_y)
grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]


at_least2 = set()

with open('input') as f:
    for line in f:
        x1y1, x2y2 = line.split('->')
        x1, y1 = x1y1.strip().split(',')
        x2, y2 = x2y2.strip().split(',')
        x1, y1, x2, y2 = x1.strip(), y1.strip(), x2.strip(), y2.strip()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] += 1
                if grid[y][x1] > 1:
                    at_least2.add((y, x1))
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] += 1
                if grid[y1][x] > 1:
                    at_least2.add((y1, x))

print('at_least2: ', len(at_least2))

'''
max_x:  989 max_y:  989
at_least2:  3990
'''

