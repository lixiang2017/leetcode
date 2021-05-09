'''
16 / 60 个通过测试用例
状态：超出时间限制
提交时间：几秒前
最后执行的输入：
[9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202]
9

DFS
Time: O(k^N)
Space: O(k)

ref:
https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/solution/gong-shui-san-xie-yi-ti-shuang-jie-jian-4epdd/
'''


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N = len(jobs)
        self.ans = 0x3f3f3f3f
        total = [0] * N

        def dfs(u, total, maximum):
            if maximum > self.ans:
                return
            if u == N:
                self.ans = maximum
                return
            
            for i in range(k):
                total[i] += jobs[u]
                dfs(u + 1, total, max(total[i], maximum))
                total[i] -= jobs[u]                

        dfs(0, total, 0)
        return self.ans



'''
approach: DFS
Time: O(k^N)
Space: O(k)

执行用时：148 ms, 在所有 Python3 提交中击败了55.24%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了31.43%的用户

ref:
https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/solution/gong-shui-san-xie-yi-ti-shuang-jie-jian-4epdd/
'''


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N = len(jobs)
        self.ans = 0x3f3f3f3f
        total = [0] * N

        def dfs(u, used, total, maximum):
            if maximum > self.ans:
                return
            if u == N:
                self.ans = maximum
                return
            
            if used < k:
                total[used] = jobs[u]
                dfs(u + 1, used + 1, total, max(total[used], maximum))
                total[used] = 0

            for i in range(used):
                total[i] += jobs[u]
                dfs(u + 1, used, total, max(total[i], maximum))
                total[i] -= jobs[u]                

        dfs(0, 0, total, 0)
        return self.ans




