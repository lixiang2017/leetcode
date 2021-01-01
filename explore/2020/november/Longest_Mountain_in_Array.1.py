'''
You are here!
Your runtime beats 32.24 % of python submissions.
'''


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        longest = 0
        size = len(A)
        # up = [0] * size
        # down = [0] * size
        up = down = 0        
        for i in range(1, size):
            if A[i - 1] == A[i] or (down and A[i - 1] < A[i]):
                up = down = 0
            if A[i - 1] < A[i]:
                up += 1
            if A[i - 1] > A[i]:
                down += 1
            if up > 0 and down > 0:
                longest = max(longest, up + down + 1)
        
        return longest
