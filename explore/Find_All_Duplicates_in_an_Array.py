'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/
You are here!
Your runtime beats 57.07 % of python submissions.
28 / 28 test cases passed.
    Status: Accepted
Runtime: 376 ms
Memory Usage: 19.5 MB
Submitted: 0 minutes ago
'''


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while (i + 1 != nums[i]) and nums[i] != nums[nums[i] - 1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]  # endless loop
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]
        
        
if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    ret = Solution().findDuplicates(nums)
    assert (ret == [2,3] or ret == [3, 2])



'''
Evaluation order
Python evaluates expressions from left to right. Notice that while evaluating an assignment, the right-hand side is evaluated before the left-hand side.
'''
