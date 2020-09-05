#
# @lc app=leetcode id=852 lang=python
#
# [852] Peak Index in a Mountain Array
#
'''
Accepted
32/32 cases passed (76 ms)
Your runtime beats 5.27 % of python submissions
Your memory usage beats 28 % of python submissions (12.8 MB)
use binary search
O(logN)
'''

# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        peak = 0
        while low <= high:  # <=
            mid = low + (high - low) / 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                peak = mid 
                break
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return peak
        
# @lc code=end

if __name__ == '__main__':
    A = [0,1,0]
    assert Solution().peakIndexInMountainArray(A) == 1

    A = [0,2,1,0]
    assert Solution().peakIndexInMountainArray(A) == 1

    A = [18,29,38,59,98,100,99,98,90]
    assert Solution().peakIndexInMountainArray(A) == 5