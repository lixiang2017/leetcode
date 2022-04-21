'''
simulation

执行用时：40 ms, 在所有 Python3 提交中击败了38.93% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了21.87% 的用户
通过测试用例：99 / 99
'''
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        goat = []
        for i, w in enumerate(sentence.split()):
            if w[0] in vowel:
                nw = w + 'ma' + 'a' * (i + 1)
            else:
                nw = w[1: ] + w[0] + 'ma' + 'a' * (i + 1)
            goat.append(nw)
        return ' '.join(goat)
