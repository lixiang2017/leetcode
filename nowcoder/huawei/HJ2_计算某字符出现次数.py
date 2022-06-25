'''
运行时间：44ms 超过28.13% 用Python 3提交的代码
占用内存：4560KB 超过61.29%用Python 3提交的代码 
'''
s = input()
target = input().strip()
s = s.lower()
target = target.lower()
ans = sum(ch == target for ch in s)
print(ans)
