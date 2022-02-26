'''
Two Pointers
T: O(N)
S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了16.09% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.33% 的用户
通过测试用例：115 / 115
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ls = list(s)
        i, j = 0, len(s) - 1
        
        def isLetter(ch):
            return ord('a') <= ord(ch) <= ord('z') or ord('A') <= ord(ch) <= ord('Z')

        while i < j:
            if not isLetter(ls[i]):
                i += 1
                continue
            if not isLetter(ls[j]):
                j -= 1
                continue
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1

        return ''.join(ls)
