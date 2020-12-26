'''
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 89.29 % of python submissions.
'''


class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        # print A
        size = len(A)
        diff = A[size - 1] - A[0]
        left, right = A[0] + K, A[size - 1] - K
        
        for i in range(size - 1):
            low = min(left, A[i + 1] - K)
            high = max(right, A[i] + K)
            diff = min(diff, high - low)
        
        return diff        
        
        