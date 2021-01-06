'''
better than Kth_Missing_Positive_Number.py and Kth_Missing_Positive_Number.1.py # in cases (arr[-1] - len(arr) < k)

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
        if arr[-1] - len(arr) < k:
            return k + len(arr)
        
        pre = 0
        count = 0
        for num in arr:
            count += num - pre - 1
            if count >= k:
                return num - (count - k) - 1
            pre = num
            
        return arr[-1] + k - count
