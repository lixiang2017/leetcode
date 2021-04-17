'''
approach: Brute Force
Time: O(N^3)
Space: O(N)

Runtime: 944 ms, faster than 5.02% of Python3 online submissions for Longest Nice Substring.
Memory Usage: 14.1 MB, less than 97.07% of Python3 online submissions for Longest Nice Substring.
'''


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        # length from N to 2
        for L in range(N, 1, -1):
            # start idx from 0 to end
            for i in range(N):
                if i + L > N:
                    break
                
                if self.isNice(s[i: i + L]):
                    return s[i: i + L]
    
        return ''

    def isNice(self, substr):
        upper = set(ord(ch) - ord('A') for ch in substr if ord('A') <= ord(ch) <= ord('Z'))
        lower = set(ord(ch) - ord('a') for ch in substr if ord('a') <= ord(ch) <= ord('z'))
        return upper == lower
