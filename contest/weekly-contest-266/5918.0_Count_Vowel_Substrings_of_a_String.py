'''
AC
two pointers + bit manipulation
T: O(N^2)
S: O(1)
'''
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        l, r = 0, 0
        N = len(word)
        need = 0
        for ch in 'aeiou':
            need |= (1 << (ord(ch) - ord('a')))
        
        now = 0
        while l < N and r < N:
            now |= (1 << (ord(word[r]) - ord('a')))
            if now & (~need):
                # contain consonants
                l = r + 1
                r += 1
                now = 0
                continue
            elif now < need:
                r += 1
                continue
            elif now == need:
                ans += 1
                
                # for part
                rr, cur = r, 0
                while rr >= l and cur != need:
                    cur |= (1 << (ord(word[rr]) - ord('a')))
                    rr -= 1
                ans += rr - l + 1
                
                r += 1
        
        return ans
