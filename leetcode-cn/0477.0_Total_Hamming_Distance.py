'''
Two Bit Arrays, T:O(32N + 32),S:O(64)

执行用时：544 ms, 在所有 Python3 提交中击败了43.50% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了86.50% 的用户
'''

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        zeros, ones = [0] * 32, [0] * 32

        for i in range(32):
            for num in nums:
                bit = (num >> i) & 1
                if 0 == bit:
                    zeros[i] += 1
                else:
                    ones[i] += 1
        
        for i in range(32):
            total += zeros[i] * ones[i]

        return total
