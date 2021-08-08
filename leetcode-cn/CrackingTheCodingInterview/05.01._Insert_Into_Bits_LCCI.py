'''
from book

执行用时：32 ms, 在所有 Python3 提交中击败了84.53% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.00% 的用户
'''
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        allOnes = ~0x0
        left = allOnes << (j + 1)
        right = (1 << i) - 1
        mask = left | right
        n_cleared = N & mask
        m_shifted = M << i
        return n_cleared | m_shifted

'''
three parts

执行用时：40 ms, 在所有 Python3 提交中击败了43.40% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了41.51%
'''
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        left = N >> (j + 1) << (j + 1)
        middle = M << i
        right = N & ((1 << i) - 1)
        return left | middle | right
