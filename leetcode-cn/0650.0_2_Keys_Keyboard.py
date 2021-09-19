'''
BFS

看到最少操作就想到了BFS。
队列中记录两个长度，一个当前长度，一个是复制或粘贴的长度。
(len_of_curr, copy_or_paste)
剪枝：对于>1000要剪掉，否则队列过长会超时。

执行用时：768 ms, 在所有 Python3 提交中击败了8.04% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了6.47% 的用户
通过测试用例：126 / 126
'''
class Solution:
    def minSteps(self, n: int) -> int:
        level = 0
        q = [(1, 0)]  # (len_of_curr, copy_or_paste)

        while q:
            next_q = []
            for qq, op in q:
                if qq == n:
                    return level
                # copy
                if qq != op and qq <= 1000:
                    next_q.append((qq, qq))
                # paste
                if op != 0 and qq + op <= 1000:
                    next_q.append((qq + op, op))

            level += 1
            q = next_q


'''
<= n

执行用时：396 ms, 在所有 Python3 提交中击败了25.18% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了8.04% 的用户
通过测试用例：126 / 126
'''
class Solution:
    def minSteps(self, n: int) -> int:
        level = 0
        q = [(1, 0)]  # (len_of_curr, copy_or_paste)

        while q:
            next_q = []
            for qq, op in q:
                if qq == n:
                    return level
                # copy
                if qq != op and qq <= n:
                    next_q.append((qq, qq))
                # paste
                if op != 0 and qq + op <= n:
                    next_q.append((qq + op, op))

            level += 1
            q = next_q


