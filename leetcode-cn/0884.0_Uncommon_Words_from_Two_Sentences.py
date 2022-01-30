'''
hash table

执行用时：36 ms, 在所有 Python3 提交中击败了43.83% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了60.80% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter((s1 + ' ' + s2).split())
        return [word for word, cnt in c.items() if cnt == 1]

'''
执行用时：32 ms, 在所有 Python3 提交中击败了75.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了21.61% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter((s1 + ' ' + s2).split())
        return [word for word in c if c[word] == 1]
        