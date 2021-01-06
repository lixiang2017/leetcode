'''
# two pointers is not necessary. # use pre
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 54.03 % of python submissions.
You are here!
Your memory usage beats 61.49 % of python submissions.
'''

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        pre = 0
        count = 0
        for num in arr:
            count += num - pre - 1
            if count >= k:
                return num - (count - k) - 1
            pre = num
            
        return arr[-1] + k - count
        