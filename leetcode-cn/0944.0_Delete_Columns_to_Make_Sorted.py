'''
执行用时：68 ms, 在所有 Python3 提交中击败了93.84% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了56.16% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                ans += 1
        return ans 

        