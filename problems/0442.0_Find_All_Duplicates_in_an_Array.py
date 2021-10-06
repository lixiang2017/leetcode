'''
Runtime: 372 ms, faster than 59.39% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.8 MB, less than 70.08% of Python3 online submissions for Find All Duplicates in an Array.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                ans.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return ans
        
        