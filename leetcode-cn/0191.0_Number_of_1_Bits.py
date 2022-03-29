'''
执行用时：16 ms, 在所有 Python 提交中击败了79.06%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了54.27%的用户
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')



'''
执行用时：16 ms, 在所有 Python 提交中击败了79.06%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了46.14%的用户
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(1 for i in range(32) if n & (1 << i))


'''
approach: Low Bit

执行用时：16 ms, 在所有 Python 提交中击败了79.06%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.28%的用户
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        while n:
            n &= (n - 1)
            ones += 1
        return ones


'''
执行用时：32 ms, 在所有 Python3 提交中击败了87.25% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了64.41% 的用户
通过测试用例：601 / 601
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n))['1']

        