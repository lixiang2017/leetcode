'''
sliding window

运行时间：42ms 超过73.91% 用Python 3提交的代码
占用内存：4740KB 超过5.65%用Python 3提交的代码 
'''
s = input()
n = int(input())
M = len(s)
gc_cnt = 0

i = 0
for i in range(n):
    if s[i] == 'G' or s[i] == 'C':
        gc_cnt += 1
        
gc_max_cnt = gc_cnt
# ans
start, end = 0, n

for i in range(n, M):
    if s[i] == 'G' or s[i] == 'C':
        gc_cnt += 1    
    if s[i - n] == 'G' or s[i - n] == 'C':
        gc_cnt -= 1
    if gc_cnt > gc_max_cnt:
        gc_cnt = gc_max_cnt 
        start, end = i - n + 1, i + 1
        
print(s[start: end])


