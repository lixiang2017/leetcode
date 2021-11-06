#! /usr/bin/python3

[x, y, n] = [int(t) for t in input().split()]
M = [[1 for j in range(y + 1)] for i in range(x + 1)]

for i in range(n):
    [a, b] = [int(t) for t in input().split()]
    M[a][b] = 0


def myfun(M, x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            if M[i][j] == 0 or (i == 0 and j == 0):
                continue
            M[i][j] = (0 if i == 0 else M[i-1][j]) + (0 if j == 0 else M[i][j-1])
    return M[x][y]

print(myfun(M, x ,y))


'''
# test case 1
3 3 2
1 1
2 2
output: 4

# test case 2
2 2 1
0 1
output: 3

# test case 3
2 2 1
1 0
output: 3

# test case 4
2 2 1
0 0
outut: 0
'''