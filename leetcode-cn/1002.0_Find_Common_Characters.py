'''
执行用时：48 ms, 在所有 Python3 提交中击败了80.29% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了82.53% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return list(reduce(operator.and_, [Counter(w) for w in words]).elements())


'''
执行用时：52 ms, 在所有 Python3 提交中击败了68.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了91.27% 的用户
通过测试用例：83 / 83
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return list(reduce(operator.and_, map(Counter, words)).elements())
        