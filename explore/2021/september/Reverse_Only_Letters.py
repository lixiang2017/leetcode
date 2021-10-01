'''
Two Pointers
T: O(N)
S: O(N)

You are here!
Your runtime beats 15.83 % of python3 submissions.
You are here!
Your memory usage beats 48.72 % of python3 submissions.
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ss = list(s)
        l , r = 0, len(ss) - 1
        while l < r:
            while l < r and not ss[l].isalpha():
                l += 1
            while l < r and not ss[r].isalpha():
                r -= 1
            if l >= r:
                break
            ss[l], ss[r] = ss[r], ss[l]
            l += 1; r -= 1
        
        return ''.join(ss)
