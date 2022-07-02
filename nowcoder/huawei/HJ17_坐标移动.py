'''
运行时间：53ms 超过17.23% 用Python 3提交的代码
占用内存：4644KB 超过70.12%用Python 3提交的代码 
'''
import sys
x = y = 0
lines = sys.stdin.readlines()[0].strip().split(';')

for line in lines:
    if 2 <= len(line) <= 3 and line[0] in 'WASD' and line[1:].isdigit():
        d = line[0] # direction
        step = int(line[1: ])
        if d == 'A':
            x -= step 
        elif d == 'D':
            x += step 
        elif d == 'W':
            y += step 
        elif d == 'S':
            y -= step 

print(x, y, sep=',')
