'''
brute force

Time Limit Exceeded
51 / 53 test cases passed.
'''



class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            # for j in range(i + 1, i + k + 1):   # IndexError: list index out of range
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
                
        return False



if __name__ == '__main__':
	nums, k, t = [1,5,9,1,5,9], 2, 3
	assert not Solution().containsNearbyAlmostDuplicate(nums, k, t)

