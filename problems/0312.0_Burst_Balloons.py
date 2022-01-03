'''
区间DP
T: O(N^3)
S: O(N^2)

Runtime: 7897 ms, faster than 70.92% of Python3 online submissions for Burst Balloons.
Memory Usage: 19.8 MB, less than 71.96% of Python3 online submissions for Burst Balloons.
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.insert(len(nums), 1)
        
        store = [[0] * len(nums) for _ in range(len(nums))]
        
        def range_best(i, j):
            # (i, j) open interval, not include i and j
            coin = 0
            for k in range(i + 1, j):
                b = nums[i] * nums[k] * nums[j]
                left = store[i][k]
                right = store[k][j]
                coin = max(coin, left + b + right)
            store[i][j] = coin
        
        # 开区间长度是3 -> len(nums)
        for range_len in range(2, len(nums)):
            # 
            for start in range(0, len(nums) - range_len):
                range_best(start, start + range_len)
        
        return store[0][len(nums) - 1]
