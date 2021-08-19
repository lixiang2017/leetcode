'''
https://leetcode-cn.com/problems/vSYUMc/
BFS * 2
关键点：两人都可以跑，小团最终一定会被小美在**死角**追到！因此统计小美和小团到达所有节点的最终时间，选择小团先到，而小美后到的**最大时间**就是答案。

执行用时：288 ms, 在所有 Python3 提交中击败了33.33% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了57.14% 的用户

ref:
https://leetcode-cn.com/problems/vSYUMc/comments/
'''
from collections import defaultdict, deque

n, x, y = list(map(int, input().split()))
# graph
g = defaultdict(list)
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

# 从 x,y 点开始 BFS
q1, q2 = deque([x]), deque([y])
visited1, visited2 = [False] * n, [False] * n
# x, y 到达所有点的最快时间
step = [[float('inf')] * 2 for _ in range(n)]
visited1[x - 1] = visited2[y - 1] = True
step[x - 1][0] = step[y - 1][1] = 0
level = 0
while q1 or q2:
    level += 1
    # xiao mei
    # 小美到达所有节点按层计数
    for _ in range(len(q1)):
        node = q1.popleft()
        for child in g[node]:
            if not visited1[child - 1]:
                q1.append(child)
                visited1[child - 1] = True
                step[child - 1][0] = level
    
    # xiao tuan
    # 小团到达所有节点按层计数
    for _ in range(len(q2)):
        node = q2.popleft()
        for child in g[node]:
            if not visited2[child - 1]:
                q2.append(child)
                visited2[child - 1] = True
                step[child - 1][1] = level

# 在所有小美晚于小团到达 i 节点的时间内挑选出最大美到达时间
print(max(m for m, t in step if m > t))


'''
输入：
5 1 2
2 1
3 1
4 2
5 3
输出：2
'''

