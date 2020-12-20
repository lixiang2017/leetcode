#! /usr/bin/python
#coding=utf-8  # for chinese characters

'''
小易从 (0,0) 点出发，每次只能选择向下走或向右走，且每一步都只能走一个单位 度，走到 (4,5) 点，计算小易一共有（）种不同行走路线。
'''

path = [[0 for i in range(5)] for j in range(6)]

path[0][0] = 0
for i in range(5):
    path[0][i] = 1

for j in range(6):
    path[j][0] = 1

for i in range(1, 6):
    for j in range(1, 5):
        print "i: ", i, "j: ", j 
        path[i][j] = path[i - 1][j] + path[i][j - 1]
        print "path[i][j]: ", path[i][j]

print path[5][4]   # 126
