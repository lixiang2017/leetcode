'''
approach: Two Pointers
Time: O(N)
Space: O(1)

67 / 67 test cases passed.
    Status: Accepted
Runtime: 1432 ms
Memory Usage: 16.3 MB
    
You are here!
Your memory usage beats 79.07 % of python submissions.
'''



class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not k: return True
        
        # remove leading 0 or rear 0
        while nums and nums[0] == 0:
            nums.pop(0)
        while nums and nums[-1] == 0:
            nums.pop(-1)
            
        size = len(nums)
        i = zeros = 0
        while i < size - 1:
            j = i + 1
            while j < size and nums[j] == 0:
                zeros += 1
                j += 1
                
            # print 'zeros: ', zeros
            if zeros < k: return False
            zeros = 0
            i = j
            
        return True
