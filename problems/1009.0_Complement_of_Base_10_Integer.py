'''
T: O(logN)
S: O(1)

Runtime: 28 ms, faster than 80.61% of Python3 online submissions for Complement of Base 10 Integer.
Memory Usage: 14.3 MB, less than 38.43% of Python3 online submissions for Complement of Base 10 Integer.
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bits = 0
        nn = n
        while n:
            bits += 1
            n >>= 1
        return (1 << bits) - 1 - nn if nn != 0 else 1
