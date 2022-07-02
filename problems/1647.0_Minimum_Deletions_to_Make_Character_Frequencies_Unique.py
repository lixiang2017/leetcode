'''
Runtime: 192 ms, faster than 69.70% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
Memory Usage: 14.8 MB, less than 51.90% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        c = sorted(Counter(s).values(), reverse=True)
        ans = 0
        for i in range(1, len(c)):
            if c[i - 1] <= c[i]:
                should = max(0, c[i - 1] - 1)
                ans += c[i] - should
                c[i] = should
        return ans
        