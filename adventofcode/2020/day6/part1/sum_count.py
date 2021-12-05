

ssum = 0

with open('input') as f:
    group = set()
    for line in f:
        line = line.strip()
        if not line:
            ssum += len(group)
            group.clear()
        else:
            group.update(list(line))

print('ssum: ', ssum)

'''
ssum:  6532
'''