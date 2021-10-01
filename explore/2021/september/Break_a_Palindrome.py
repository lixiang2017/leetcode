'''
T: O(N)
S: O(N)

You are here!
Your runtime beats 82.30 % of python3 submissions.
You are here!
Your memory usage beats 46.55 % of python3 submissions.
'''
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = palindrome
        N = len(p)
        # a b c d e f ... z
        if N <= 1:
            return ''
        
        pl = list(p)
        # aaaaaaaaaaaaaa   # aaaa x aaaa
        if set(pl) == {'a'} or set(pl[: N // 2]) == {'a'}:
            pl[-1] = 'b'
            return ''.join(pl)
            
        for i, ch in enumerate(pl):
            if ch != 'a':
                pl[i] = 'a'
                return ''.join(pl)
