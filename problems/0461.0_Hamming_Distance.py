'''
Runtime: 28 ms, faster than 85.04% of Python3 online submissions for Hamming Distance.
Memory Usage: 14.3 MB, less than 12.51% of Python3 online submissions for Hamming Distance.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


'''
remove low bit step by step

Runtime: 28 ms, faster than 85.04% of Python3 online submissions for Hamming Distance.
Memory Usage: 14.3 MB, less than 12.51% of Python3 online submissions for Hamming Distance.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans, xor = 0, x ^ y
        while xor:
            xor &= (xor - 1)
            ans += 1
        return ans
