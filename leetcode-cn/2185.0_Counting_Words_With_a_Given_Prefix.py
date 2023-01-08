'''
执行用时：40 ms, 在所有 Python3 提交中击败了53.81% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了21.19% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)

'''
执行用时：40 ms, 在所有 Python3 提交中击败了53.81% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了32.63% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w[: len(pref)] == pref for w in words)
             