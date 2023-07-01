'''
执行用时：40 ms, 在所有 Python3 提交中击败了70.19% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了23.08% 的用户
通过测试用例：266 / 266
'''
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range(n):
            if words[i][-1] != words[(i + 1) % n][0]:
                return False
        return True


'''
执行用时：52 ms, 在所有 Python3 提交中击败了7.69% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了46.63% 的用户
通过测试用例：266 / 266
'''
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        return all(words[i][-1] == words[(i + 1) % n][0] for i in range(n))
        