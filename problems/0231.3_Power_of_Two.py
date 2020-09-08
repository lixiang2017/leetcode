#! /usr/bin/python
# #! /usr/local/bin/python3

from math import log

class Solution(object):
    """
    :type n: int
    :rtype: bool
    """
    def isPowerOfTwo(self, n):
        return log(n, 2).is_integer() if n > 0 else False


if __name__ == "__main__":
    n = 1
    assert Solution().isPowerOfTwo(n)

    n = 16
    assert Solution().isPowerOfTwo(n)

    n = 218
    assert not Solution().isPowerOfTwo(n) 

    n = 0
    assert not Solution().isPowerOfTwo(n)

    n = 536870912
    assert Solution().isPowerOfTwo(n)

"""
Wrong Answer
Input:
536870912
Output:
false
Expected:
true

536870912 = 1024 * 1024 * 512 = 2 ** 29
log(536870912, 2) = 29.000000000000004
python2中math.log(x[, base])有精度损失
"""
