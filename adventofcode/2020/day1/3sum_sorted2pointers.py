#! /bin/python
'''
solution: sort + two pointers
Time: O(n ^ 2)
'''

entries = []
with open('input') as input:
    for one in input:
        entries.append(int(one))

entries = sorted(entries)
size = len(entries)
print 'the length of entries is ', size
SUM = 2020

for i in range(size):
    j = i + 1
    k = size - 1
    if i > 0 and entries[i] == entries[i - 1]:
        continue

    while j < k:
        if k < size - 1 and entries[k] == entries[k + 1]:
            k -= 1
            continue
        sum3 = entries[i] + entries[j] + entries[k]
        if sum3 > SUM:
            k -= 1
            continue
        elif sum3 < SUM:
            j += 1
            continue
        else:
            print 'the 3 indice are ', i, j, k
            print 'the 3 numbers are ', entries[i],  entries[j], entries[k]
            product = entries[i] * entries[j] * entries[k]
            print 'the product is ', product
            k -= 1
            j += 1



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

'''
the length of entries is  200
the 3 indice are  1 7 8
the 3 numbers are  332 830 858
the product is  236430480
'''


