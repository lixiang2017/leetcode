'''
Runtime: 103 ms, faster than 85.88% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 66.20% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = -1
        for j, x in enumerate(nums):
            if j == 0 or nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        
        