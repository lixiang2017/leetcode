#! /usr/local/bin/python3
# #! /usr/bin/python

# 0 & -1 -> 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            return n & (n - 1) == 0


if __name__ == "__main__":
    n = 1
    assert Solution().isPowerOfTwo(n)

    n = 16
    assert Solution().isPowerOfTwo(n)

    n = 218
    assert not Solution().isPowerOfTwo(n) 

    n = 0
    assert not Solution().isPowerOfTwo(n)