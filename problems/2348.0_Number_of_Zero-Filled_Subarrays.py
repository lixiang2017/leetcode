'''
Runtime: 1087 ms, faster than 78.80% of Python3 online submissions for Number of Zero-Filled Subarrays.
Memory Usage: 24.7 MB, less than 30.39% of Python3 online submissions for Number of Zero-Filled Subarrays.
'''
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = zero = 0
        for x in nums:
            if x == 0:
                zero += 1
            else:
                ans += zero * (zero + 1) // 2
                zero = 0
        
        return ans + zero * (zero + 1) // 2


'''
Runtime: 1073 ms, faster than 83.39% of Python3 online submissions for Number of Zero-Filled Subarrays.
Memory Usage: 24.5 MB, less than 78.09% of Python3 online submissions for Number of Zero-Filled Subarrays.
'''
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = zero = 0
        for x in nums:
            if x == 0:
                zero += 1
            else:
                zero = 0
            ans += zero
        
        return ans
        