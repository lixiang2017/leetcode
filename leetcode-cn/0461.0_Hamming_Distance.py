'''
Bit Manipulation,T:O(32),S:O(1)

执行用时：60 ms, 在所有 Python3 提交中击败了7.55% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.57% 的用户
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming = 0
        while x or y:
            if (x & 1) != (y & 1):
                hamming += 1
            x >>= 1
            y >>= 1

        return hamming


'''
执行用时：52 ms, 在所有 Python3 提交中击败了7.55% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.57% 的用户
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([1 for i in range(32) if (x & (1<<i) != (y & (1 << i)))])


'''
执行用时：48 ms, 在所有 Python3 提交中击败了14.94% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.57% 的用户
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


'''
执行用时：32 ms, 在所有 Python3 提交中击败了95.78% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.57% 的用户
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        hamming = 0
        while z:
            hamming += z & 1
            z >>= 1
        return hamming

