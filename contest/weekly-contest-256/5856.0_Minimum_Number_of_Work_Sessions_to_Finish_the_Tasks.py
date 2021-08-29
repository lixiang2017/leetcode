'''
必须用spares[:]才行

75 / 75 个通过测试用例
状态：通过
执行用时: 600 ms
内存消耗: 15.2 MB
提交时间：2 小时前
'''

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        N = len(tasks)
        ans = 14
        def dfs(i: int, spares: List[int], session: int):
            nonlocal ans
            if session >= ans:
                return 
            if i == N:
                ans = min(ans, session)
                return
            
            # do it in spares
            spares.sort(reverse=True)
            for j, spare in enumerate(spares):
                if spare >= tasks[i]:
                    # do it
                    spares[j] -= tasks[i]
                    dfs(i + 1, spares[:], session)
                    # recover
                    spares[j] += tasks[i]
                else:
                    # can not do it any more
                    break

            # do it with a new session
            slot = sessionTime - tasks[i]
            if slot > 0:
                spares.append(slot)
            dfs(i + 1, spares[:], session + 1)
            if slot > 0:
                spares.pop()

        dfs(0, [], 0)
        return ans

'''
输入：[3,6,5,5,10,7]
10
输出：3
预期：4
'''
