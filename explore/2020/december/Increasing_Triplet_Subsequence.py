'''
You are here!
Your runtime beats 20.94 % of python submissions.

Time: O(N)  # O(N * 3)
Space: O(N)  # O(N * 2)
'''



class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        forward = [nums[0] for _ in range(size)]
        backward = [nums[-1] for _ in range(size)]
        
        for i in range(1, size):
            forward[i] = min(forward[i - 1], nums[i])
        for j in range(size - 2, 0, -1):
            backward[j] = max(backward[j + 1], nums[j])
        
        # print forward
        # print backward
        
        for i in range(size):
            if forward[i] < nums[i] < backward[i]:
                return True
        return False
