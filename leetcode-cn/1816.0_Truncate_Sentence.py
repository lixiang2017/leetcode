'''
执行用时：36 ms, 在所有 Python3 提交中击败了32.34% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了43.87% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[: k])
        