'''
Bit Manipulation

执行用时：32 ms, 在所有 Python3 提交中击败了79.41% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.37% 的用户
通过测试用例：992 / 992
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # overflow
        MIN, MAX = - 1 << 31, (1 << 31) - 1
        if dividend == MIN and divisor == -1:
            return MAX

        negative = (dividend ^ divisor) < 0
        t, d = abs(dividend), abs(divisor)
        ans = 0
        for i in range(31, -1, -1):
            if (t >> i) >= d:
                ans += 1 << i
                t -= d << i
        return [ans, -ans][negative]
        
