
tree_map = []

with open('input') as f:
    for line in f:
        line = line.strip()
        tree_map.append(line)

M, N = len(tree_map), len(tree_map[0])


def get_tree_cnt(dx, dy):
    t = 0
    i = j = 0
    while i < M:
        if tree_map[i][j] == '#':
            t += 1
        i += dy
        j += dx
        j %= N 

    return t 


slops = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for dx, dy in slops:
    t = get_tree_cnt(dx, dy)
    print('dx, dy: ', (dx, dy), 'tree: ', t)
    product *= t 

print('product: ', product)


'''
dx, dy:  (1, 1) tree:  61
dx, dy:  (3, 1) tree:  257
dx, dy:  (5, 1) tree:  64
dx, dy:  (7, 1) tree:  47
dx, dy:  (1, 2) tree:  37
product:  1744787392
'''