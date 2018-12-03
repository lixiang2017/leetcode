"""
使用位运算。
for example:
5: 0101
4: 0100
0100（&=）
3: 0011
0000（&=）
按位与赋值每次可以消除一个1。
如果1在末尾，n-1只有末尾与n不同，位与赋值后消去末尾的1。
如果1不在末尾，n-1从n的最低位1之后每一位都与n不同，位与赋值之后消去n最低位的1。
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt

if __name__ == "__main__":
    n = 11
    print(Solution().hammingWeight(n))
    n = 128
    print(Solution().hammingWeight(n))
    n = 63
    print(Solution().hammingWeight(n))