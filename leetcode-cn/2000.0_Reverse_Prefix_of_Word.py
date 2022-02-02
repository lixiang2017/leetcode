'''
执行用时：40 ms, 在所有 Python3 提交中击败了9.37% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.35% 的用户
通过测试用例：112 / 112
'''
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        else:
            return word[: idx + 1][:: -1] + word[idx + 1: ]
