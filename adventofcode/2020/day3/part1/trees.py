
tree_map = []

with open('input') as f:
    for line in f:
        line = line.strip()
        tree_map.append(line)

M, N = len(tree_map), len(tree_map[0])
t = 0
start = -3
for row in tree_map:
    start += 3
    start %= N
    if row[start] == '#':
        t += 1

print('t: ', t)

'''
t:  257
'''