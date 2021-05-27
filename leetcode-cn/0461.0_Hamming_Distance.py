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