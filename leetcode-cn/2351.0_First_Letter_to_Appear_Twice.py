'''
执行用时：44 ms, 在所有 Python3 提交中击败了16.86% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了72.22% 的用户
通过测试用例：92 / 92
'''
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch 
            seen.add(ch)

'''
执行用时：32 ms, 在所有 Python3 提交中击败了86.31% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了72.22% 的用户
通过测试用例：92 / 92
'''
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mask = 0
        for ch in s:
            if (1 << (ord(ch) - ord('a'))) & mask:
                return ch 
            mask |= 1 << (ord(ch) - ord('a'))
                        