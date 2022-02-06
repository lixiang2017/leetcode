'''
执行用时：40 ms, 在所有 Python3 提交中击败了11.09% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了31.52% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern) == len(s.split()) and len(set(pattern)) == len(set(s.split())) == len(set(zip(pattern, s.split())))
        