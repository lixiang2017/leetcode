'''
执行用时：36 ms, 在所有 Python3 提交中击败了75.06% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了7.65% 的用户
通过测试用例：79 / 79
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return 26 == len(set(sentence))


'''
执行用时：36 ms, 在所有 Python3 提交中击败了75.06% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了95.31% 的用户
通过测试用例：79 / 79
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = 0
        for ch in sentence:
            x |= (1 << (ord(ch) - ord('a')))
        return x == ((1 << 26) - 1)
        