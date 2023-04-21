'''
binary search
T: O(NlogN)
S: O(1)

Runtime: 2123 ms, faster than 13.01% of Python3 online submissions for Minimize Maximum of Array.
Memory Usage: 26.8 MB, less than 39.46% of Python3 online submissions for Minimize Maximum of Array.
'''
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        def check(m):
            rem = 0
            for i in range(n - 1, -1, -1):
                if nums[i] > m:
                    rem += nums[i] - m
                else:
                    rem -= min(rem, m - nums[i])
            return rem == 0
        
        l, r = min(nums), max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1

'''
greedy + prefix sum
T: O(N)
S: O(1)

Runtime: 809 ms, faster than 73.09% of Python3 online submissions for Minimize Maximum of Array.
Memory Usage: 26 MB, less than 84.30% of Python3 online submissions for Minimize Maximum of Array.
'''
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = pre = 0
        for i, x in enumerate(nums):
            pre += x
            ans = max(ans, (pre + i) // (i + 1))
        return ans
        
