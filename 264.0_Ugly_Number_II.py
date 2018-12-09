# Time Limit Exceeded


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 7:
            return n
        cnt = 6
        i = 6
        while cnt < n:
            i += 1
            if self.isUgly(i):
                cnt += 1

        return i

    def isUgly(self, i):
        while i % 3 == 0:
            i /= 3
        while i % 5 == 0:
            i /= 5
        return int(i) & int(i-1) == 0



if __name__ == "__main__":
    n = 1
    assert Solution().nthUglyNumber(n) == 1
    n = 2
    assert Solution().nthUglyNumber(n) == 2
    n = 3
    assert Solution().nthUglyNumber(n) == 3
    n = 4
    assert Solution().nthUglyNumber(n) == 4
    n = 5
    assert Solution().nthUglyNumber(n) == 5
    n = 6
    assert Solution().nthUglyNumber(n) == 6
    n = 7
    assert Solution().nthUglyNumber(n) == 8
    n = 100
    assert Solution().nthUglyNumber(n) == 1536
    print(Solution().nthUglyNumber(n))
    n = 224   # Time Limit Exceeded
    print(Solution().nthUglyNumber(n))
    n = 1000
    assert Solution().nthUglyNumber(n) == 51200000
    print(Solution().nthUglyNumber(n))

 #   n = 1690
 #   print(Solution().nthUglyNumber(n))