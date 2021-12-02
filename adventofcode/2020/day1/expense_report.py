#! /bin/python
'''
Two Sum
'''

entries = []
with open('input') as input:
    for one in input:
        entries.append(int(one))

size = len(entries)
print 'the length of entries is ', size

SUM = 2020

# need = [0 for _ in range(size)]
need = {}
for i in range(size):
    if entries[i] in need:
        product = entries[need[entries[i]]] * entries[i]
        print 'product', product
    need[SUM - entries[i]] = i

'''
the length of entries is  200
1224 796
product 974304
'''

