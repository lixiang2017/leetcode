'''
Time Limit Exceeded

'''



class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product < k:
                    count += 1
                else:
                    break
                    
        return count
                
if __name__ == '__main__':
	nums = [10, 5, 2, 6]
	k = 100
	assert Solution().numSubarrayProductLessThanK(nums, k) == 8