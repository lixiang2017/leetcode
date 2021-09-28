'''
61 / 61 test cases passed.
    Status: Accepted
Runtime: 516 ms
Memory Usage: 16.6 MB
    
Submitted: 0 minutes ago

You are here!
Your memory usage beats 42.23 % of python3 submissions.
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = r = 0
        while l < len(nums):
            while l < len(nums) and l & 1 == nums[l] & 1:
                l += 1
            if l >= len(nums):
                break
            r = l + 1
            while r < len(nums) and l & 1 != nums[r] & 1:
                r += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            
        return nums
