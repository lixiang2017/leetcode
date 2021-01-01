'''
Runtime Error

Wrong Answer
'''



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        max_n = max(nums)
        for i in range(1, max_n + 1):   # need to use xrange 
            if i not in nums:
                return i
        return max_n + 1


if __name__ == '__main__':
    nums = [1,2,0]
    assert Solution().firstMissingPositive(nums) == 3

    nums = [3,4,-1,1]
    assert Solution().firstMissingPositive(nums) == 2

    nums = [7,8,9,11,12]
    assert Solution().firstMissingPositive(nums) == 1

    nums = []
    assert Solution().firstMissingPositive(nums) == 1

    nums = [2147483647]
    assert Solution().firstMissingPositive(nums) == 1

    nums = [-5]
    assert Solution().firstMissingPositive(nums) == 1    