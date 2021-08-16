'''
Two Pointers

执行用时：32 ms, 在所有 Python3 提交中击败了89.55% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了57.98% 的用户
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        M, N = len(s), len(t)
        while i < M and j < N:
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
        return i == M
