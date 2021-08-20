'''
执行用时：24 ms, 在所有 Python3 提交中击败了98.80% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了98.57% 的用户
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[:: -1], s.split()))
        