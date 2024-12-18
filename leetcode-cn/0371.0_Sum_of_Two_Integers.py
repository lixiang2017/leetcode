'''
Iteration
执行用时：36 ms, 在所有 Python3 提交中击败了66.47%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了36.51%的用户

ref:
https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 2 ^ 32
        MASK = 0x100000000
        MM = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~(a ^ MM)


'''
输入：
-12
-8
输出：
-8589934573
预期结果：
-20
'''



'''
Recursion

执行用时：32 ms, 在所有 Python3 提交中击败了83.33%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了18.85%的用户
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 2 ^ 32
        MASK = 0x100000000
        MM = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000

        if 0 == b:
            return a if a <= MAX_INT else ~(a ^ MM)

        carry = (a & b) << 1
        a = (a ^ b) % MASK
        b = carry % MASK                    
        return self.getSum(a, b)


'''
执行用时：32 ms, 在所有 Python3 提交中击败了59.27% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了27.34% 的用户
通过测试用例：13 / 13
'''
# 因为Python中整数是无限长的，无论怎么左移都不会溢出，所以需要限制一下长度。
M1 = (1 << 32)
M2 = (1 << 31)
M3 = (1 << 31) - 1

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            xor = (a ^ b) % M1
            carry = ((a & b) << 1) % M1
            a, b = xor, carry

        if a & M2:
            return ~(a ^ M2 ^ M3)
        else:
            return a
            