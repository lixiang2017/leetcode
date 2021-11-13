'''
执行用时：32 ms, 在所有 Python3 提交中击败了68.45% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了53.35% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.match('^[A-Z]*$|^[a-z]*$|^[A-Z][a-z]*$', word) != None


'''
执行用时：28 ms, 在所有 Python3 提交中击败了87.65% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了92.07% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.match('^([A-Z]*|[a-z]*|[A-Z][a-z]*)$', word) != None


'''
执行用时：36 ms, 在所有 Python3 提交中击败了41.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了53.35% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.match('^([A-Z]+|[a-z]+|[A-Z][a-z]+)$', word) != None


'''
执行用时：32 ms, 在所有 Python3 提交中击败了68.45% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.72% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.search('^([A-Z]+|[a-z]+|[A-Z][a-z]+)$', word) != None


'''
执行用时：28 ms, 在所有 Python3 提交中击败了87.65% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了43.90% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


'''
执行用时：36 ms, 在所有 Python3 提交中击败了41.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.49% 的用户
通过测试用例：550 / 550
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.title()


'''
执行用时：36 ms, 在所有 Python3 提交中击败了41.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了17.99% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()
        


'''
执行用时：24 ms, 在所有 Python3 提交中击败了96.34% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了65.70% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.match('^([A-Z]*|[a-z]*|[A-Z][a-z]*)$', word) is not None


'''
执行用时：36 ms, 在所有 Python3 提交中击败了41.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.69% 的用户
通过测试用例：550 / 550
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = 0
        for ch in word:
            if ord('a') <= ord(ch) <= ord('z'):
                lower += 1
        return lower == 0 or lower == len(word) or \
            lower == (len(word) - 1) and (ord('A') <= ord(word[0]) <= ord('Z'))
            