'''
提交结果：答案正确 运行时间：56ms 占用内存：4548KB 使用语言：Python 3 用例通过率：100.00%
'''
s = input()
n = len(s)
i = n - 1
ans = 0
while i >= 0 and s[i] != ' ':
    ans += 1
    i -= 1
print(ans)


'''
运行时间：43ms 超过37.87% 用Python 3提交的代码
占用内存：4644KB 超过5.08%用Python 3提交的代码 
'''
s = input()
print(len(s.strip().split()[-1]))

