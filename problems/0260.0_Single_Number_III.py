'''
异或分组
T: O(2N)
S: O(1)

Runtime: 56 ms, faster than 91.30% of Python3 online submissions for Single Number III.
Memory Usage: 15.6 MB, less than 95.73% of Python3 online submissions for Single Number III.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda x, y: x ^ y, nums)
        lowbit = xor - (xor & (xor - 1))
        
        a = b = 0
        for x in nums:
            if lowbit & x:
                a ^= x
            else:
                b ^= x
        
        return a, b



'''
异或分组
T: O(2N)
S: O(1)

Runtime: 64 ms, faster than 57.17% of Python3 online submissions for Single Number III.
Memory Usage: 15.8 MB, less than 84.86% of Python3 online submissions for Single Number III.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda x, y: x ^ y, nums)
        # lowbit = xor - (xor & (xor - 1))
        # get its last set bit
        lowbit  = xor & (-xor)
        
        a = b = 0
        for x in nums:
            if lowbit & x:
                a ^= x
            else:
                b ^= x
        
        return a, b
        


'''
it does not need to XOR for both group in the second pass. XOR for one group suffices.

Runtime: 60 ms, faster than 77.46% of Python3 online submissions for Single Number III.
Memory Usage: 15.7 MB, less than 95.73% of Python3 online submissions for Single Number III.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda x, y: x ^ y, nums)
        # lowbit = xor - (xor & (xor - 1))
        # get its last set bit
        lowbit  = xor & (-xor)
        
        a = b = 0
        for x in nums:
            if lowbit & x:
                a ^= x
        b = a ^ xor
        
        return a, b
        


