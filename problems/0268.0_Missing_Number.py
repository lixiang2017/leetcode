class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)

if __name__ == "__main__":
    nums = [3, 0, 1]
    assert Solution().missingNumber(nums) == 2

    nums = [9,6,4,2,3,5,7,0,1]
    assert Solution().missingNumber(nums) == 8


'''
Runtime: 153 ms, faster than 72.96% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 77.27% of Python3 online submissions for Missing Number.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)