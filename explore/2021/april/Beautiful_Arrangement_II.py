'''
approach: Reverse left array each time
Time: O(N * K)
Space: O(N)

68 / 68 test cases passed.
Status: Accepted
Runtime: 860 ms
Memory Usage: 15.1 MB
Submitted: 0 minutes ago
'''

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = list(range(1, n + 1))
        for i in range(1, k):
            ans[i:] = ans[: i - 1: -1]
        return ans
