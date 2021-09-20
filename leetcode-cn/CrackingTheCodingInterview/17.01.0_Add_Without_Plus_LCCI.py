'''
执行用时：32 ms, 在所有 Python3 提交中击败了71.78% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.45% 的用户
通过测试用例：51 / 51

-1
2
'''
import ctypes
class Solution:
    def add(self, a: int, b: int) -> int:
        # only add, no carry
        if 0 == a:
            return b
        if 0 == b:
            return a
            
        xor = a ^ b
        carry = (a & b) << 1
        carry = ctypes.c_int32(carry).value
        return self.add(xor, carry)


'''
执行用时：96 ms, 在所有 Python3 提交中击败了6.93% 的用户
内存消耗：32.1 MB, 在所有 Python3 提交中击败了5.45% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        import numpy as np 
        while b:
            xor = a ^ b
            carry = (a & b) << 1
            a = np.int32(xor)
            b = np.int32(carry)
        return int(a)


'''
执行用时：28 ms, 在所有 Python3 提交中击败了87.19% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了88.18% 的用户
通过测试用例：51 / 51
'''
MAX_BIT = 2 ** 32
MAX_BIT_COMPLIMENT = -2 ** 32
class Solution:
    def add(self, a: int, b: int) -> int:
        while b != 0:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            carry = a & b
            a ^= b
            b = carry << 1
        return a

