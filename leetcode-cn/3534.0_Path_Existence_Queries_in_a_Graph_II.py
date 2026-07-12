"""倍增"""


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        # 按战力排序，order[k] 表示排序后第 k 个位置对应的原节点
        idx = sorted(range(n), key=lambda i: nums[i])

        # values：排序后的战力数组
        values = [nums[node] for node in idx]

        # pos[node]：原节点 node 在排序后数组里所在的位置
        pos = [0] * n
        for rank, node in enumerate(idx):
            pos[node] = rank

        m = (
            n
        ).bit_length()  # m=log2(n)+1 ，表示倍增的最大层数；如n=5时，m=3，表示最多可以跳2^2=4步
        farthest = [[0] * m for _ in range(n)]

        # k = 0：一步最远射程（双指针滑动窗口）
        right = 0
        for left in range(n):
            right = max(right, left)
            while right + 1 < n and values[right + 1] - values[left] <= maxDiff:
                right += 1
            farthest[left][0] = right  # f[i][0] = 从 i 跳 1 步能到达的最右位置

        # k >= 1：两段拼接，指数级扩展
        for k in range(1, m):
            for i in range(n):
                farthest[i][k] = farthest[farthest[i][k - 1]][k - 1]
                # 状态转移方程：从i跳2^j步 = 先从i跳2^(j-1)步到中间点，再从中间点跳2^(j-1)步

        res = []

        for u, v in queries:
            l, r = pos[u], pos[v]  # 将原始节点编号转换为排序后的排名
            if l > r:
                l, r = r, l  # 保证 l <= r，因为我们只关心从左到右的距离
            if l == r:
                res.append(0)  # 特殊情况：同一个节点，距离为0
                continue
            step = 0
            for i in range(m - 1, -1, -1):
                if farthest[l][i] < r:
                    l = farthest[l][i]  # 没到r，执行这次跳跃
                    step += 1 << i  # 累加实际跳跃步数（2^i步！）

            if farthest[l][0] >= r:  # 到达或超过r
                res.append(step + 1)  # 把最后1步加上
            else:
                res.append(-1)  # 无法到达，不连通

        return res
