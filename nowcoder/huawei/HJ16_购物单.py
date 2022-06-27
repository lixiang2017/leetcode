'''
运行时间：162ms 超过92.48% 用Python 3提交的代码
占用内存：7564KB 超过53.39%用Python 3提交的代码 

0-1背包的变形
把 主件和附件 的组合情况，提前计算出来。最多只有四种情况。
1、仅主件
2、主件 + 附件1
3、主件 + 附件2
4、主件 + 附件1 + 附件2

每件物品的价格（都是 10 元的整数倍） => 可以都 //10 处理
1-indexed 都减去1，改成 0-indexed
'''
from collections import defaultdict 

money, total = map(int, input().strip().split())
money //= 10
main2annex = defaultdict(list)
vs = [0] * total   # value
ps = [0] * total   # importance

for i in range(total):
    v, p, q = map(int, input().strip().split())
    v //= 10
    vs[i] = v 
    ps[i] = p
    if 0 == q:
        if i not in main2annex:
            main2annex[i] = [] 
    else:
        q -= 1
        main2annex[q].append(i)

# main_idx ->  [price, importance]
pi = defaultdict(list)
for m, annexes in main2annex.items():
    # only one main
    pi[m].append([vs[m], vs[m]*ps[m]])
    if len(annexes) == 1:
        a = annexes[0]
        pi[m].append([vs[m] + vs[a], vs[m]*ps[m] + vs[a]*ps[a]])
    elif len(annexes) == 2:
        a1, a2 = annexes[0], annexes[1]
        pi[m].append([vs[m] + vs[a1], vs[m]*ps[m] + vs[a1]*ps[a1]])
        pi[m].append([vs[m] + vs[a2], vs[m]*ps[m] + vs[a2]*ps[a2]])
        pi[m].append([vs[m] + vs[a1] + vs[a2], vs[m]*ps[m] + vs[a1]*ps[a1] + vs[a2]*ps[a2]])

n = len(pi)
dp = [[0] * (money + 1) for _ in range(n + 1)]

i = 0
for m, pis in pi.items():
    i += 1
    for j in range(money + 1):
        t = dp[i - 1][j]
        for pr, im in pis: 
            if j >= pr:
                t = max(t, dp[i - 1][j - pr] + im)
        dp[i][j] = t

print(dp[n][money] * 10) 


