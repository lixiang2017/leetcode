'''
DFS
假设u有四个孩子节点v1, v2, v3, v4.
            u
        /   |   \   \
      v1    v2  v3   v4
假设当前u节点计算的个数为res, 结果为
res * (dfs(v1) + 1) * (dfs(v2) + 1) * (dfs(v3) + 1) * (dfs(v4) + 1)

ref：
https://leetcode-cn.com/problems/Uo7Dr5/solution/meituan-001-xiao-mei-de-yong-hu-ming-by-awua1/
https://leetcode-cn.com/problems/Uo7Dr5/solution/mei-ju-zui-xiao-zhi-dfs-by-minori-s6ci/


执行用时：20 ms, 在所有 Python3 提交中击败了98.95% 的用户
内存消耗：9.3 MB, 在所有 Python3 提交中击败了14.14% 的用户
通过测试用例：10 / 10
'''
n, k = list(map(int, input().split()))
# graph
g = [[] for _ in range(n + 1)]
# n - 1 edges
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
# level 
A = [0]
A += list(map(int, input().split()))
MOD = 1_000_000_007

# to find between [A[i], A[i] + k]
def dfs(u, fa, i):
    res = 1
    for child in g[u]:
        if child == fa: continue
        if A[child] < A[i] or A[child] > A[i] + k: continue
        # need later nodes
        if A[child] == A[i] and child < i: continue
        res = res + res * dfs(child, u, i)
        res %= MOD

    return res

# main
ans = 0
for node in range(1, n + 1):
    ans += dfs(node, 0, node)
    ans %= MOD
print(ans)


'''
输入：
5 1
1 2
2 3
3 4
4 5
2 2 2 2 2
输出：15
解释：显然一个区域的方案有 {1}，{2}，{3}，{4}，{5}，两个区域的方案有 4 个，三个区域的方案有 3 个，四个区域的方案有 2 个，五个区域的方案有 1 个，共 15 个。
'''
