'''
approach: backtracking
'''


import numpy
import math
from pprint import pprint


# N = 5
N = 4
# N = 3
result = []

def backtracking(path = []):
    global N
    if len(path) == N:
        result.append(path)

    for i in range(N):
        if i in path:
            # break # wrong!
            continue

        backtracking(path + [i])

# driver
backtracking([])


pprint(numpy.math.factorial(N))
pprint(math.factorial(N))
pprint(len(result))
pprint(result)


# print len(result)
# print result

'''
24
24
24
[[0, 1, 2, 3],
 [0, 1, 3, 2],
 [0, 2, 1, 3],
 [0, 2, 3, 1],
 [0, 3, 1, 2],
 [0, 3, 2, 1],
 [1, 0, 2, 3],
 [1, 0, 3, 2],
 [1, 2, 0, 3],
 [1, 2, 3, 0],
 [1, 3, 0, 2],
 [1, 3, 2, 0],
 [2, 0, 1, 3],
 [2, 0, 3, 1],
 [2, 1, 0, 3],
 [2, 1, 3, 0],
 [2, 3, 0, 1],
 [2, 3, 1, 0],
 [3, 0, 1, 2],
 [3, 0, 2, 1],
 [3, 1, 0, 2],
 [3, 1, 2, 0],
 [3, 2, 0, 1],
 [3, 2, 1, 0]]
'''


