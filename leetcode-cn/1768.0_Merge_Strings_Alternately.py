'''
执行用时：36 ms, 在所有 Python3 提交中击败了75.95% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了55.06% 的用户
通过测试用例：108 / 108
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        seq = []
        for a, b in zip_longest(word1, word2, fillvalue=''):
            seq.append(a)
            seq.append(b)
        return ''.join(seq)
        