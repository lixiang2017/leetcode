'''
Runtime: 892 ms, faster than 71.06% of Python3 online submissions for Count Subarrays With Fixed Bounds.
Memory Usage: 28.7 MB, less than 41.16% of Python3 online submissions for Count Subarrays With Fixed Bounds.
'''
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l, r1, r2, ans = -1, -1, -1, 0
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                l = i
            if x == minK:
                r1 = i
            if x == maxK:
                r2 = i
            ans += max(0, min(r1, r2) - l)
        return ans 
    
    