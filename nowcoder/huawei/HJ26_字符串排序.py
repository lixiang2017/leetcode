'''
运行时间：43ms 超过65.50% 用Python 3提交的代码
占用内存：4616KB 超过58.79%用Python 3提交的代码 
'''
import sys
s = sys.stdin.readline().strip()
n = len(s)
letters = [''] * 26

ans = list(s)
for ch in s:
    if ch.isalpha():
        lch = ch.lower()
        letters[ord(lch) - ord('a')] += ch 
i = 0
for part in letters:
    if not part:
        continue
    for ch in part:
        while not ans[i].isalpha():
            i += 1
        ans[i] = ch 
        i += 1

print(''.join(ans))




'''
运行时间：56ms 超过11.50% 用Python 3提交的代码
占用内存：4596KB 超过79.71%用Python 3提交的代码 
'''
import sys
s = sys.stdin.readline().strip()
n = len(s)
ss = sorted(filter(str.isalpha, s), key=str.lower)

ans = list(s)
i = j = 0
while i < len(ss):
    while not ans[j].isalpha():
        j += 1
    ans[j] = ss[i]
    j += 1
    i += 1
print(''.join(ans))

