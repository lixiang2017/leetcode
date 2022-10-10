'''
T: O(N)
S: O(N)

Runtime: 51 ms, faster than 55.08% of Python3 online submissions for Break a Palindrome.
Memory Usage: 13.8 MB, less than 61.62% of Python3 online submissions for Break a Palindrome.
'''
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = palindrome
        if len(p) == 1:
            return ''
        pl = list(p)
        n = len(p)
        all_a = True 
        for i, ch in enumerate(pl):
            if ch != 'a' and not (n % 2 == 1 and n // 2 == i):
                pl[i] = 'a'
                all_a = False 
                break 
        if not all_a:
            return ''.join(pl)
        else:
            pl[-1] = 'b'
            return ''.join(pl)
                