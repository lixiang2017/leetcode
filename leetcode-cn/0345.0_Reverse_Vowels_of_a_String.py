'''
Two Pointers

执行用时：44 ms, 在所有 Python3 提交中击败了95.90% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了81.81% 的用户
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        l, r = 0, len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while l < r:
            while l < r and ss[l] not in vowels:
                l += 1
            while l < r and ss[r] not in vowels:
                r -= 1
            if l >= r:
                break
            else:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
        return ''.join(ss)

'''
Two Pointers

执行用时：44 ms, 在所有 Python3 提交中击败了95.80% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了58.40% 的用户
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        ss = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and ss[l] not in vowels:
                l += 1
            while l < r and ss[r] not in vowels:
                r -= 1
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1
        
        return ''.join(ss)
