'''
two pointers

执行用时：32 ms, 在所有 Python3 提交中击败了84.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了78.43% 的用户
通过测试用例：137 / 137
'''
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1, sentence2 = sentence1.split(), sentence2.split()
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        m, n = len(sentence1), len(sentence2)
        i = 0
        while i < n and sentence1[i] == sentence2[i]:
            i += 1
        if i == n:
            return True 
        j1, j2 = m - 1, n - 1
        while j2 >= i and sentence1[j1] == sentence2[j2]:
            j1 -= 1
            j2 -= 1
        return j2 + 1 == i 

'''
deque

执行用时：40 ms, 在所有 Python3 提交中击败了46.08% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了53.92% 的用户
通过测试用例：137 / 137
'''
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = deque(sentence1.split()), deque(sentence2.split())
        while words1 and words2:
            if words1[0] == words2[0]:
                words1.popleft()
                words2.popleft()
            elif words1[-1] == words2[-1]:
                words1.pop()
                words2.pop()
            else:
                return False
        return True

'''
list

执行用时：40 ms, 在所有 Python3 提交中击败了46.08% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了48.04% 的用户
通过测试用例：137 / 137
'''
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        while words1 and words2:
            if words1[0] == words2[0]:
                words1.pop(0)
                words2.pop(0)
            elif words1[-1] == words2[-1]:
                words1.pop()
                words2.pop()
            else:
                return False
        return True

'''
two pointers

执行用时：32 ms, 在所有 Python3 提交中击败了84.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了78.43% 的用户
通过测试用例：137 / 137
'''
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        m, n = len(words1), len(words2)
        i, j1, j2 = 0, m - 1, n - 1
        while i <= j1 and i <= j2:
            if words1[i] == words2[i]:
                i += 1
            elif words1[j1] == words2[j2]:
                j1 -= 1
                j2 -= 1
            else:
                return False
        return True
