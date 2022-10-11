'''
执行用时：52 ms, 在所有 Python3 提交中击败了9.72% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.42% 的用户
通过测试用例：131 / 131
'''
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True 
        diff = [[a, b] for a, b in zip(s1, s2) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][:: -1]
        