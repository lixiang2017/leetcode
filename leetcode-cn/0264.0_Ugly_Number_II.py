'''
Brute Force

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
Time: O( (sqrt3(N))^3 + NlogN ) = O(N + NlogN) = O(NlogN)
Space: O(N)

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


'''
approach: Heap + Set
Time: O(NlogN)
Space: O(N)

执行用时：364 ms, 在所有 Python 提交中击败了28.63%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了27.45%的用户
'''

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        seen = {1}
        factors = [2, 3, 5]

        for i in range(n - 1):
            top = heapq.heappop(heap)
            for factor in factors:
                if top * factor not in seen:
                    seen.add(top * factor)
                    heapq.heappush(heap, top * factor)
                
        return heapq.heappop(heap)


'''
approach: DP/Iteration + Three Pointers
Time: O(N)
Space: O(N)

执行用时：96 ms, 在所有 Python 提交中击败了87.84%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了90.59%的用户
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            # elif dp[i] == num3:  # elif will be wrong, because nums2, num3 or num5 can be equal. 
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]

