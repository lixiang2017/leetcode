'''
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 68.60 % of python submissions.
You are here!
Your memory usage beats 90.70 % of python submissions.
'''


class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = k
        for num in nums:
            if num == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
                
        return True
