'''
intuition

You are here!
Your runtime beats 94.74 % of python submissions.
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
        # up = down = 0        
        i = 0
        while i < size - 1:
            while i < size - 1 and A[i] >= A[i + 1]: i += 1
            peak = i
            while peak < size - 1 and A[peak] < A[peak + 1]: peak += 1
            j = peak
            while j < size - 1 and A[j] > A[j + 1]: j += 1
            if i < peak < j: longest = max(longest, j - i + 1)
            i = j
        
        return longest
        