'''

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了78.95%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了67.42%的用户
'''


class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        repeat = 0
        while word * (repeat + 1) in sequence:
            repeat += 1
        return repeat


'''
approach: Binary

ref:
https://leetcode-cn.com/problems/maximum-repeating-substring/solution/python-er-fen-fa-by-miaoch-mpee/

执行结果：
通过
显示详情
执行用时：12 ms, 在所有 Python 提交中击败了93.23%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了71.97%的用户
'''


class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        L, R = 0, len(sequence) / len(word)
        while L < R:
            # mid = L + (R - L) // 2 # TLE
            mid = L + (R - L + 1) // 2
            if word * mid in sequence:
                L = mid
            else:
                R = mid - 1
        return L

'''
执行用时：36 ms, 在所有 Python3 提交中击败了70.09% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了72.22% 的用户
通过测试用例：212 / 212
'''
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while word * (k + 1) in sequence:
            k += 1
        return k
        