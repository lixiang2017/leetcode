'''
Runtime: 798 ms, faster than 90.41% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
Memory Usage: 28.6 MB, less than 13.68% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        for left in range(n):
            right = bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                ans += pow(2, right - left, MOD)
            else:
                break
        
        return ans % MOD
        

'''
Runtime: 816 ms, faster than 77.88% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
Memory Usage: 28.7 MB, less than 12.40% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += pow(2, right - left, MOD)
                left += 1
            else:
                right -= 1   
        return ans % MOD
        
'''
Runtime: 789 ms, faster than 93.99% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
Memory Usage: 28.6 MB, less than 14.83% of Python3 online submissions for Number of Subsequences That Satisfy the Given Sum Condition.
'''
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                right -= 1
        
        return ans
        

        