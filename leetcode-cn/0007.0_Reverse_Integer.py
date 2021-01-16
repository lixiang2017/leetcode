'''
执行结果：
通过
显示详情
执行用时：
44 ms
, 在所有 Python 提交中击败了
7.20%
的用户
内存消耗：
13.1 MB
, 在所有 Python 提交中击败了
26.69%
的用户
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            x = -x
            isNegative = True
        # x = int(str(x).reverse())
        x = int(''.join(list(reversed(str(x)))) )
        if - 2 ** 31 > x or x > 2 ** 31 - 1: return 0

        return -x if isNegative else x

'''
输入：
1534236469
输出：
9646324351
预期结果：
0

输入：
1563847412
输出：
2147483651
预期结果：
0

 If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

'''

