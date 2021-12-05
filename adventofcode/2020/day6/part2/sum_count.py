

ssum = 0

with open('input') as f:
    group = set()
    isFirstLine = True
    for line in f:
        line = line.strip()
        if not line:
            ssum += len(group)
            group.clear()
            isFirstLine = True
        else:
            if isFirstLine:
                group = set(list(line))
                isFirstLine = False
            else:
                group = group.intersection(list(line))

print('ssum: ', ssum)

'''
ssum:  3427
'''
