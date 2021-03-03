'''
Time: O(N)
Space: O(1)

执行用时：
100 ms, 在所有 Python 提交中击败了53.97%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了96.83%的用户
'''

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        diff = max(A) - min(A) - 2 * K 
        return diff if diff > 0 else 0

'''
执行用时：96 ms, 在所有 Python 提交中击败了68.25%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了69.84%的用户
'''

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2 * K)