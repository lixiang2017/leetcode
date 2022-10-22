'''
执行用时：60 ms, 在所有 Python3 提交中击败了66.77% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了52.72% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for l in range(n - 1, 0, -1):
            if n % l == 0:
                times = n // l 
                if s[: l] * times == s:
                    return True 
        return False


'''
执行用时：92 ms, 在所有 Python3 提交中击败了58.89% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了52.72% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return any(len(s) % l == 0 and s[: l] * (len(s) // l) == s  for l in range(len(s) - 1, 0, -1))
