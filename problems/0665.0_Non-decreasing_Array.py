'''
T: O(N)
S: O(1)

Runtime: 372 ms, faster than 13.40% of Python3 online submissions for Non-decreasing Array.
Memory Usage: 15.2 MB, less than 49.84% of Python3 online submissions for Non-decreasing Array.
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # mess count, mess index left 
        cnt, idx = 0, -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                idx = i
        if cnt > 1:
            return False 
        elif cnt == 0:
            return True 
        if idx == 0 or idx == len(nums) - 2:
            return True 
        return nums[idx] <= nums[idx + 2] or nums[idx - 1] <= nums[idx + 1] 

'''
Input
[5,7,1,8]
Output
false
Expected
true

Input
[-1,4,2,3]
Output
false
Expected
true
'''
        
