#! /bin/python

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
    #if entries[i] in need:
    #    product = entries[need[entries[i]]] * entries[i]
    #    print entries[need[entries[i]]], entries[i]
    #    print 'product', product
    need[SUM - entries[i]] = i

for need_sum, index in need.iteritems():
    for i in range(size - 1):
        for j in range(i + 1, size):
            if entries[i] + entries[j] == need_sum:
                print 'three indice are ', i, j, index
                print 'the three numbers are ', entries[i], entries[j], entries[index]
                product = entries[i] * entries[j] * entries[index]
                print 'product is ', product


'''
the length of entries is  200
product 974304
'''

'''
the length of entries is  200
three indice are  134 170 61
the three numbers are  858 830 332
product is  236430480
three indice are  61 134 170
the three numbers are  332 858 830
product is  236430480
three indice are  61 170 134
the three numbers are  332 830 858
product is  236430480
'''
