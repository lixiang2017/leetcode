'''
执行用时：36 ms, 在所有 Python3 提交中击败了86.35% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了54.62% 的用户
通过测试用例：1146 / 1146
'''
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        elif m == n:
            diff_cnt = sum(1 for f, s in zip(first, second) if f != s)
            return diff_cnt <= 1
        else:
            q1, q2 = deque(list(first)), deque(list(second))
            while q1 and q2 and q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
            while q1 and q2 and q1[-1] == q2[-1]:
                q1.pop()
                q2.pop()
            return len(q1) +  len(q2) == 1
