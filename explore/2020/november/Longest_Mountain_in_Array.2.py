'''
You are here!
Your runtime beats 86.18 % of python submissions.
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
        for i in range(1, size - 1):
            if A[i - 1] < A[i] > A[i + 1]:  # find the peak first
                left, right = i - 1, i + 1
                while left > 0 and A[left - 1] < A[left]: left -= 1
                while right < size - 1 and A[right] > A[right + 1]: right += 1
                longest = max(longest, right - left + 1)
        
        return longest
        