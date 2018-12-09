# Time Limit Exceeded


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = sorted(2 ** a * 3 ** b * 5 ** c for a in range(42) for b in range(28) for c in range(14))
        return ugly[n-1]


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
    n = 224
    assert Solution().nthUglyNumber(n) == 25000
    n = 1000
    assert Solution().nthUglyNumber(n) == 51200000
    n = 1680
    assert Solution().nthUglyNumber(n) == 2025000000
    n = 1690    # 2123366400
    assert Solution().nthUglyNumber(n) == 2123366400
