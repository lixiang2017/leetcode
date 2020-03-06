'''
Success
Details 
Runtime: 68 ms, faster than 68.19% of Python online submissions for Power of Three.
Memory Usage: 11.9 MB, less than 9.52% of Python online submissions for Power of Three.
'''

import sys
import math
# sys.maxint == 9223372036854775807
# 4294967296
# 2147483647        2^32 -1
# math.pow(3, 19) == 1162261467.0


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_value = 1162261467
        return n > 0 and (max_value % n == 0)


if __name__ == "__main__":
    n = 27
    assert Solution().isPowerOfThree(n)

    n = 0
    assert not Solution().isPowerOfThree(n)

    n = 9
    assert Solution().isPowerOfThree(n)

    n = 45
    assert not Solution().isPowerOfThree(n)
