'''
执行用时：36 ms, 在所有 Python3 提交中击败了55.42% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.63% 的用户
通过测试用例：40 / 40
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        l = r = 0
        for ch in s:
            if ch == 'L':
                l += 1
            elif ch == 'R':
                r += 1
            if l == r:
                ans += 1
                l = r = 0

        return ans
