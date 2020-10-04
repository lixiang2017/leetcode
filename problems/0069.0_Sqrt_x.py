import math

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))


if __name__ == "__main__":
    x = 4
    assert Solution().mySqrt(x) == 2

    x = 8
    assert Solution().mySqrt(x) == 2
