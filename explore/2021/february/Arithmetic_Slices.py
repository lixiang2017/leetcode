'''
approach: Two Pointers + Math
Time: O(N)
Space: O(1)

n: (n - 3 + 1)
(n - 2) + (n - 3) + (n - 4) + ... + 1 = (n - 1) *  (n - 2) / 2
'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        slices = 0
        left, right = 0, len(A)
        n = 0
        while left + 1 < right:
            n = 0
            start = left
            pre_diff = A[start + 1] - A[start]
            while start + 1 < right and A[start + 1] - A[start] == pre_diff:
                n += 1
                start += 1
            
            if n >= 2:
                slices += (n) *  (n - 1) / 2
            
            # left = start + 1  # wrong answer!
            left =  start
      
        return slices
        