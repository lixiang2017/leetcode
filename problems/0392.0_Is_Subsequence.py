'''
two pointers
T: O(M + N)
S: O(1)

Runtime: 60 ms, faster than 23.50% of Python3 online submissions for Is Subsequence.
Memory Usage: 14 MB, less than 55.23% of Python3 online submissions for Is Subsequence.
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        i = j = 0
        while i < ns and j < nt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
                
        return i == ns
