'''
You are here!
Your runtime beats 63.74 % of python3 submissions.
You are here!
Your memory usage beats 84.62 % of python3 submissions.
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if 1 == k:
            return min(s[i:] + s[:i] for i in range(len(s)))
        return ''.join(sorted(s))