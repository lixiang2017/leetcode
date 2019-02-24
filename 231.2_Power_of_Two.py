#! /usr/local/bin/python3
# #! /usr/bin/python

from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return log2(n).is_integer() if n > 0 else False


if __name__ == "__main__":
    n = 1
    assert Solution().isPowerOfTwo(n)

    n = 16
    assert Solution().isPowerOfTwo(n)

    n = 218
    assert not Solution().isPowerOfTwo(n) 

    n = 0
    assert not Solution().isPowerOfTwo(n)