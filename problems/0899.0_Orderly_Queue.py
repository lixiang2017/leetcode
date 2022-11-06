'''
Runtime: 72 ms, faster than 9.52% of Python3 online submissions for Orderly Queue.
Memory Usage: 13.9 MB, less than 72.62% of Python3 online submissions for Orderly Queue.
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if 1 == k:
            return min(s[i: ] + s[: i] for i in range(len(s)))
        return ''.join(sorted(s))
        