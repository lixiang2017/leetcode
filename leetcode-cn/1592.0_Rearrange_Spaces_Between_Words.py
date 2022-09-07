'''
执行用时：32 ms, 在所有 Python3 提交中击败了89.82% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了55.64% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        words = text.split()
        words_len = sum(len(word) for word in words)
        words_cnt = len(words)
        if words_cnt == 1:
            return words[0] + ' ' * (n - words_len)
        else:
            space_cnt = n - words_len
            q, r = divmod(space_cnt, words_cnt - 1)
            return (' ' * q).join(words) + ' ' * r
        