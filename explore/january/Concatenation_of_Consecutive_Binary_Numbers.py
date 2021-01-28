'''
Time: O(N)
Space: O(1)

ref:
https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers/solution/lian-jie-lian-xu-er-jin-zhi-shu-zi-by-ze-t40j/
# mod # 加法减法乘法对取余运算有分配律
https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers/solution/c-ni-xu-bian-li-chu-yu-ding-li-by-treasu-njq4/
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-quotient-remainder-theorem
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication
https://www.zhihu.com/question/41361614
# 
除余定理：

模的四则运算：
(a + b) % p = (a % p + b % p) % p
(a - b) % p = (a % p - b % p ) % p
(a * b) % p = (a % p * b % p) % p
a ^ b % p = ((a % p)^b) % p
结合律：
((a+b) % p + c) % p = (a + (b+c) % p) % p
((ab) % p * c)% p = (a * (bc) % p) % p
交换律：
(a + b) % p = (b+a) % p
(a * b) % p = (b * a) % p
分配律：
(a+b) % p = ( a % p + b % p ) % p
((a +b)% p * c) % p = ((a * c) % p + (b * c) % p) % p




You are here!
Your runtime beats 67.18 % of python submissions.
You are here!
Your memory usage beats 56.07 % of python submissions.
'''

class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        value = 0
        shift = 0
        for i in range(1, n + 1):
            if not i & (i - 1):
                shift += 1
            value = ((value << shift) + i) % MOD
        
        return value
    