'''
sliding window
T: O(N)
S: O(1)

Runtime: 177 ms, faster than 72.84% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
Memory Usage: 17.2 MB, less than 14.59% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current = 0
        vowel = set('aeiou')
        i, n = 0, len(s)
        while i < k:
            if s[i] in vowel:
                current += 1
            i += 1
        ans = current
        while i < n:
            if s[i] in vowel:
                current += 1
            if s[i - k] in vowel:
                current -= 1
            ans = max(ans, current)
            i += 1
        return ans
