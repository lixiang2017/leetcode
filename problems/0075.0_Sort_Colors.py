'''
T: O(N)
S: O(1)

Runtime: 32 ms, faster than 83.16% of Python3 online submissions for Sort Colors.
Memory Usage: 14.2 MB, less than 47.04% of Python3 online submissions for Sort Colors.

https://en.wikipedia.org/wiki/Dutch_national_flag_problem
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1
            
'''
T: O(NlogN)

Runtime: 36 ms, faster than 63.58% of Python3 online submissions for Sort Colors.
Memory Usage: 13.8 MB, less than 99.96% of Python3 online submissions for Sort Colors.s
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
