'''
执行用时：124 ms, 在所有 Python3 提交中击败了60.99% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了69.23% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        next_need_cnt = len(s) + 5
        for cnt in sorted(c.values(), reverse=True):
            if cnt >= next_need_cnt:
                ans += cnt - next_need_cnt
                next_need_cnt -= 1
            else:
                next_need_cnt = cnt - 1 
            next_need_cnt = max(next_need_cnt, 0)
        return ans 

'''
执行用时：116 ms, 在所有 Python3 提交中击败了73.63% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了98.90% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        c = sorted(Counter(s).values(), reverse=True)
        ans = 0
        for i in range(1, len(c)):
            if c[i - 1] <= c[i]:
                should = max(0, c[i - 1] - 1)
                ans += c[i] - should
                c[i] = should
        return ans
        