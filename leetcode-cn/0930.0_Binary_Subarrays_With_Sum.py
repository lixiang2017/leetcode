'''
Hash Table
'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = pre = 0
        freq = defaultdict(int)
        for num in nums:
            freq[pre] += 1
            pre += num
            total += freq[pre - goal]
        return total
