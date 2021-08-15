'''
https://leetcode-cn.com/problems/GXV5dX/

执行用时：152 ms, 在所有 Python3 提交中击败了67.86% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了35.71% 的用户
'''
from heapq import heapify, heappop

s = input().split()
n, m = int(s[0]), int(s[1])
v, w, price = [], [], []
i = 0
while i < n:
    vw = input().split()
    v.append(int(vw[0]))
    w.append(int(vw[1]))
    price.append((-(v[-1] + w[-1] * 2), i))
    i += 1

heapify(price)
ans = []
while m:
    ans.append(heappop(price)[1] + 1)
    m -= 1

print(' '.join((str(p) for p in sorted(ans))))

'''
输入：
5 2
5 10
8 9
1 4
7 9
6 10
输出：2 5
'''
