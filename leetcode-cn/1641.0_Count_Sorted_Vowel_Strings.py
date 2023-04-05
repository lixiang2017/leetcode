'''
DP

执行用时：32 ms, 在所有 Python3 提交中击败了89.86% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了24.64% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = a, a + e, a + e + i, a + e + i + o, a + e + i + o + u
        return a + e + i + o + u


'''
执行用时：36 ms, 在所有 Python3 提交中击败了75.36% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了11.60% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def count(n, last_idx):
            if n == 1:
                return last_idx + 1
            return sum(count(n - 1, i) for i in range(last_idx + 1))
            
        return count(n, 4)

'''
执行用时：40 ms, 在所有 Python3 提交中击败了47.83% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了94.93% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4)
        