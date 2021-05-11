'''
approach: Directly change X to Y, Greedy + Iteration.
看官方题解和其他用户的题解都是各种逆向计算，其实这不必要，以下展示正向计算的思路。
只需要讨论 Y > X时的情况。分为两步统计， cnt1为多少个乘法，cnt2为多少个减法。
显然我们必须把 X 乘到恰好比 Y 大的数，否则再怎么减也达不到要求……因此先求 cnt1.
那么，关键是 cnt2 怎么求呢？
我们假设减法穿插在各个乘法之间，如果在第一次乘法前减，那么最终等价于减去 2^{cnt1}
 , 如果在第二次乘法前减，最终等价于减去 2^{cnt1 - 1}
 ，以此类推。由于每次可以减多个1，因此最终要乘个系数，减了 a * 2^{cnt1} + b * 2^{cnt1 - 1} + ....
那么这个系数 a,b,c等等是多少呢，贪心即可，a越大越好，其次到b, c...

Time: O(log(Y/X)), it's more obvious than reversion in Broken_Calculator.py
Space: O(1)

ref:
https://leetcode-cn.com/problems/broken-calculator/solution/wu-xu-ni-xiang-zheng-xiang-ji-suan-jian-ji-zheng-m/
https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC%2B%2BPython-Change-Y-to-X-in-1-Line

感想：
现在LCCN（中文站）比LCUS（美国站）要好很多了。不用一味地以为美国站好。
1. 中文站中很多题解已经很全面了。就拿这一题的正向题解来说，美国站只有题解没有解释，中国站可以找到解释，瞬间就懂了。
不过，可以去美国站也看看。学习对应的计算机术语和表述。或许还有一些新奇的解法。
'''



class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        operations = 0
        multiple = 1
        while X * multiple < Y:
            multiple <<= 1
            operations += 1
        diff = X * multiple - Y
        while diff > 0:
            operations += diff / multiple
            diff -= diff / multiple * multiple
            multiple >>= 1

        return operations
