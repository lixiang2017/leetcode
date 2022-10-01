'''
执行用时：44 ms, 在所有 Python3 提交中击败了31.02% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了91.02% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if s1 == s2 == "":
            return True
        return len(s1) == len(s2) and any(s1[i: ] + s1[: i] == s2 for i in range(len(s1)))

'''
执行用时：44 ms, 在所有 Python3 提交中击败了31.02% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了51.19% 的用户
通过测试用例：31 / 31
'''
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2 * 2 
        