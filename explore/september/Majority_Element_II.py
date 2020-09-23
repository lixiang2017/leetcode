'''
Boyer-Moore Majority Vote Algorithm

You are here!
Your runtime beats 94.94 % of python submissions.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
        	return []

        num1 = num2 = nums[0]
        time1, time2 = 0, 0
        for num in nums:
        	if num1 == num:
        		time1 += 1
        	elif num2 == num:
        		time2 += 1
        	elif time1 == 0:
        		num1 = num
        		time1 += 1
        	elif time2 == 0:
        		num2 = num
        		time2 += 1
        	else:
        		time1 -= 1
        		time2 -= 1

        time1 = time2 = 0
        for num in nums:
        	if num == num1:
        		time1 += 1
        	elif num == num2:
        		time2 += 1
        res = []
        n = len(nums)
        if time1 > n / 3:
        	res.append(num1)
        if time2 > n / 3:
        	res.append(num2)

        return res


if __name__ == '__main__':
	nums = [3,2,3]
	assert Solution().majorityElement(nums) == [3]

	nums = [1,1,1,3,3,2,2,2]
	assert Solution().majorityElement(nums) == [1,2]