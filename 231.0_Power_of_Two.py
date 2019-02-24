#! /usr/local/bin/python3
# #! /usr/bin/python

# Time Limit Exceeded
# Last executed input: 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        if n == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    n = 1
    assert Solution().isPowerOfTwo(n)

    n = 16
    assert Solution().isPowerOfTwo(n)

    n = 218
    assert not Solution().isPowerOfTwo(n) 