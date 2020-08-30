'''
You are here!
Your runtime beats 54.11 % of python submissions.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        num_counts = Counter(nums)
        return num_counts.most_common()[0][0]



if __name__ == '__main__':
	nums = [3,2,3]
	assert Solution().majorityElement(nums) == 3

	nums = [2,2,1,1,1,2,2]
	assert Solution().majorityElement(nums) == 2
