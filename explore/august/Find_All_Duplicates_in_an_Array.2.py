'''
You are here!
Your runtime beats 83.61 % of python submissions.
28 / 28 test cases passed.
    Status: Accepted
Runtime: 340 ms
Memory Usage: 19.7 MB
Submitted: 0 minutes ago
'''


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return ans
        
        
if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    ret = Solution().findDuplicates(nums)
    assert (ret == [2,3] or ret == [3, 2])
