'''
You are here!
Your runtime beats 19.08 % of python submissions.
'''



class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        longest = 0
        size = len(A)
        up = [0] * size
        down = [0] * size
        for i in range(size - 2, 0, -1):
            if A[i] > A[i + 1]:
                down[i] = down[i + 1] + 1
        
        for i in range(1, size - 1):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1
            if up[i] > 0 and down[i] > 0:
                longest = max(longest, up[i] + down[i] + 1)
        
        return longest
        