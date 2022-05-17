'''
执行用时：36 ms, 在所有 Python3 提交中击败了76.76% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了37.65% 的用户
通过测试用例：120 / 120
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ol = dict(zip(order, string.ascii_lowercase))
        prev = ''
        for word in words:
            trans = ''.join(map(ol.__getitem__, word))
            if prev > trans:
                return False
            prev = trans 
        return True

'''
执行用时：48 ms, 在所有 Python3 提交中击败了12.16% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了35.49% 的用户
通过测试用例：120 / 120
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: [order.index(ch) for ch in w])
        