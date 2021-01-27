'''
Time: O(N)
Space: O(1)

ref:
https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers/solution/lian-jie-lian-xu-er-jin-zhi-shu-zi-by-ze-t40j/

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
    