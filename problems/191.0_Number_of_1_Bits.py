class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return format(n, 'b').count('1')

if __name__ == "__main__":
    n = 11
    print(Solution().hammingWeight(n))
    n = 128
    print(Solution().hammingWeight(n))