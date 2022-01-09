'''
执行用时：32 ms, 在所有 Python3 提交中击败了66.96% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了7.67% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def maxDepth(self, s: str) -> int:
        maxd = left = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                left -= 1
            maxd = max(maxd, left)

        return maxd 

