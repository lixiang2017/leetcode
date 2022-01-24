'''
执行用时：32 ms, 在所有 Python3 提交中击败了82.59% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了42.04% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
        