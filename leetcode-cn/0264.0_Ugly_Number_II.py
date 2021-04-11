'''
395 / 596 个通过测试用例
状态：超出时间限制
提交时间：几秒前
最后执行的输入：
396
'''


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nth = 0
        i = 1
        while True:
            if self.isUgly(i):
                nth += 1
                if nth == n:
                    return i
            i += 1
    
    def isUgly(self, i):
        for mod in [2, 3, 5]:
            while i % mod == 0:
                i /= mod
        return i == 1


'''
approach: Math + Iteration

执行用时：2924 ms, 在所有 Python 提交中击败了5.10%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了5.10%的用户
'''
'''
1690 
In [26]: 14 * 14 * 14
Out[26]: 2744
In [27]: 13 * 13 * 13
Out[27]: 2197
In [28]: 12 * 12 * 12
Out[28]: 1728
#
In [29]: 5 ** 13
Out[29]: 1220703125
In [30]: 2 ** 31
Out[30]: 2147483648
In [31]: 3 ** 21
Out[31]: 10460353203
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = set()
        for i in range(31):
            for j in range(21):
                for k in range(14):
                    ugly = (2 ** i) * (3 ** j) * (5 ** k)
                    uglys.add(ugly)
        u = sorted(list(uglys))
        return u[n - 1]

