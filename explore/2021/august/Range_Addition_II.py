'''
You are here!
Your runtime beats 15.50 % of python3 submissions.
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        minm, minn = 10**8, 10**8
        for a, b in ops:
            minm = min(minm, a)
            minn = min(minn, b)
        return minm * minn
