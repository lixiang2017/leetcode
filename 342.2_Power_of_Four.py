'''
Success
Details 
Runtime: 12 ms, faster than 96.84% of Python online submissions for Power of Four.
Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Power of Four.
'''
'''
# reference
https://leetcode.com/problems/power-of-four/discuss/80464/My-non-loop-solution-with-no-relation-to-the-bit-length-of-int

# 思考：这三个条件的组合是不是充分必要条件呢？
条件2 限制为偶数。
偶数可分为两种情况，即 2^(2n) 和 2^(2n+1) 两种情况。
即 4^n 和 2*(4^n) 两种
## 二项式定理
4^n = (3 + 1)^n             mod 3, must be 1
2*(4^n) = 2 * (3 + 1)^n     mod 3, must be 2
因此，是充分必要条件。
'''



class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and not (num & (num - 1)) and (num % 3 == 1)

if __name__ == "__main__":
    num = 16
    assert Solution().isPowerOfFour(num)

    num = 5
    assert not Solution().isPowerOfFour(num)

    num = 0
    assert not Solution().isPowerOfFour(num)
