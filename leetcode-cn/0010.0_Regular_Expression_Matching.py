'''
执行用时：56 ms, 在所有 Python3 提交中击败了37.43% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.15% 的用户
通过测试用例：353 / 353
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match('^' + p + '$', s))

'''
执行用时：60 ms, 在所有 Python3 提交中击败了27.61% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了81.81% 的用户
通过测试用例：353 / 353
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match(p + '$', s))
        