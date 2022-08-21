'''
one line

执行用时：36 ms, 在所有 Python3 提交中击败了73.86% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了49.79% 的用户
通过测试用例：40 / 40
'''
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next((i + 1 for i, word in enumerate(sentence.split()) if word.startswith(searchWord)), -1)
