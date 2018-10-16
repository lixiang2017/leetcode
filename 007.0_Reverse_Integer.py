class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            x = -x
            if x < 0:
                return 0
            s = str(x)
            s = s[::-1]
            x = int(s)
            if x < 0 or x > ((1 << 31) - 1):
                return 0
            else:
                return -x

        else:
            s = str(x)
            s = s[::-1]
            x = int(s)
            if x < 0 or x > ((1 << 31) - 1):
                return 0
            else:
                return x


if __name__ == "__main__":
    x = 123
    print(Solution().reverse(x))

    x = -123
    print(Solution().reverse(x))

    x = 120
    print(Solution().reverse(x))

    x = 1200000000000000000000000
    print(Solution().reverse(x))

    x = -120000000000000000000
    print(Solution().reverse(x))

    x = 12000000000000000000034985
    print(Solution().reverse(x))
    x = -120000000000000000000879
    print(Solution().reverse(x))

    print(1 << 31)