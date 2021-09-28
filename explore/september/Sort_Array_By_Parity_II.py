'''
Two Pointers
T: O(N^2)
S: O(1)

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

'''
Two Pointers
T: O(N)
S: O(1)

You are here!
Your runtime beats 54.85 % of python3 submissions.
You are here!
Your memory usage beats 73.54 % of python3 submissions.
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i, j = 0, 1
        while i < N and j < N:
            if nums[i] & 1:
                while j < N and nums[j] & 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
            i += 2
        return nums


'''
Two Pointers
T: O(N)
S: O(1)

You are here!
Your runtime beats 30.34 % of python3 submissions.
You are here!
Your memory usage beats 88.11 % of python3 submissions
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = r = 0
        while l < len(nums):
            while l < len(nums) and l & 1 == nums[l] & 1:
                l += 1
            if l >= len(nums):
                break
            if r == 0 or r == l:
                r = l + 1

            while r < len(nums) and ((l & 1 != nums[r] & 1) or (r & 1 == l & 1)):
                r += 1
            if r >= len(nums):
                break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

        return nums




