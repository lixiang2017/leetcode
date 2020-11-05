'''
Approach: Mathematical
Complexity Analysis
 Time Complexity: O(N), where N is the length of A.
 Space Complexity: O(1)



Success
Details 
Runtime: 92 ms, faster than 71.72% of Python online submissions for Smallest Range I.
Memory Usage: 14.7 MB, less than 46.46% of Python online submissions for Smallest Range I.
'''

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_a = max(A)
        min_a = min(A)
        
        if min_a + K >= max_a - K:
            return 0
        else:
            return max_a - K - (min_a + K)
