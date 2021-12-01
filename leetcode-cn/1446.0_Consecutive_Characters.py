'''
执行用时：32 ms, 在所有 Python3 提交中击败了95.67% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了23.81% 的用户
通过测试用例：333 / 333
'''
class Solution:
    def maxPower(self, s: str) -> int:
        pre, cnt, ans = '', 0, 0
        for ch in s:
            if pre == ch:
                cnt += 1
            else:
                pre = ch
                cnt = 1
            ans = max(ans, cnt)
        return ans
