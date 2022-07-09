'''
from left to right 
sliding window + heap

Runtime: 2165 ms, faster than 15.57% of Python3 online submissions for Jump Game VI.
Memory Usage: 37.4 MB, less than 5.50% of Python3 online submissions for Jump Game VI.
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n 
        dp[0] = nums[0]
        h = [(-nums[0], 0)]
        # from left to right 
        for i in range(1, n):
            # cannot reach i 
            while h and h[0][1] + k < i:
                heappop(h)
            j = h[0][1]
            dp[i] = max(dp[i], dp[j] + nums[i])
            heappush(h, (-dp[i], i))          
        return dp[-1]

'''
no need to use max

Runtime: 1755 ms, faster than 34.60% of Python3 online submissions for Jump Game VI.
Memory Usage: 36.6 MB, less than 10.06% of Python3 online submissions for Jump Game VI.
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n 
        dp[0] = nums[0]
        h = [(-nums[0], 0)]
        # from left to right 
        for i in range(1, n):
            # cannot reach i 
            while h and h[0][1] + k < i:
                heappop(h)
            j = h[0][1]
            dp[i] = dp[j] + nums[i]
            heappush(h, (-dp[i], i))          
        return dp[-1]

'''
in place. use nums array, no need to use dp array

Runtime: 1175 ms, faster than 84.59% of Python3 online submissions for Jump Game VI.
Memory Usage: 33.1 MB, less than 31.60% of Python3 online submissions for Jump Game VI.
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = [(-nums[0], 0)]
        # from left to right 
        for i in range(1, n):
            # cannot reach i 
            while h and h[0][1] + k < i:
                heappop(h)
            j = h[0][1]
            nums[i] += nums[j]
            heappush(h, (-nums[i], i))          
        return nums[-1]


'''
# from right to left 
sliding window + heap

Runtime: 2740 ms, faster than 5.04% of Python3 online submissions for Jump Game VI.
Memory Usage: 36.6 MB, less than 10.06% of Python3 online submissions for Jump Game VI.
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n 
        dp[-1] = nums[-1]
        h = [(-nums[-1], n - 1)]
        # from right to left 
        for i in range(n - 2, -1, -1):
            # cannot reach i 
            while h and i + k < h[0][1]:
                heappop(h)
            j = h[0][1]
            dp[i] = dp[j] + nums[i]
            heappush(h, (-dp[i], i))
        return dp[0]

'''
in place. use nums array, no need to use dp array

Runtime: 2461 ms, faster than 7.87% of Python3 online submissions for Jump Game VI.
Memory Usage: 34.3 MB, less than 25.79% of Python3 online submissions for Jump Game VI.
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = [(-nums[-1], n - 1)]
        # from right to left 
        for i in range(n - 2, -1, -1):
            # cannot reach i 
            while h and i + k < h[0][1]:
                heappop(h)
            j = h[0][1]
            nums[i] += nums[j]
            heappush(h, (-nums[i], i))
        return nums[0]





