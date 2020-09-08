#
# @lc app=leetcode id=852 lang=python
#
# [852] Peak Index in a Mountain Array
#
'''
Accepted
32/32 cases passed (56 ms)
Your runtime beats 92.47 % of python submissions
Your memory usage beats 36 % of python submissions (12.8 MB)
O(N)
'''

# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        for i in range(1, l):
            if A[i] > A[i-1]:
                continue
            else: # A[i] < A[i-1]
                return i-1
                

# @lc code=end

if __name__ == '__main__':
    A = [0,1,0]
    assert Solution().peakIndexInMountainArray(A) == 1

    A = [0,2,1,0]
    assert Solution().peakIndexInMountainArray(A) == 1
