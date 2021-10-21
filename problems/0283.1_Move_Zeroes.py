'''
Two Pointers
T: O(N)
S: O(1)

Runtime: 234 ms, faster than 20.18% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.4 MB, less than 66.52% of Python3 online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        N = len(nums)
        while j < N:
            while j < N and nums[j] == 0:
                j += 1
            if j >= N:
                break
            nums[i] = nums[j]
            i += 1
            j += 1
        while i < N:
            nums[i] = 0
            i += 1


'''
Runtime: 309 ms, faster than 13.21% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.7 MB, less than 5.66% of Python3 online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i, x in enumerate(nums):
            if x:
                nums[pos], nums[i] = x, nums[pos]
                pos += 1
                