'''
sliding window

You are here!
Your runtime beats 98.92 % of python submissions.
'''




class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        prod = 1
        left = 0
        for i in range(len(nums)):
        	prod *= nums[i]
        	while (left <= i and prod >= k):
        		prod /= nums[left]
        		left += 1
        	res += i - left + 1
        return res
                
if __name__ == '__main__':
	nums = [10, 5, 2, 6]
	k = 100
	print Solution().numSubarrayProductLessThanK(nums, k)
	# assert Solution().numSubarrayProductLessThanK(nums, k) == 8