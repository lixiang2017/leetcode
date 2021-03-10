'''
approach: Greedy
intuition: next permutation
Time: O(N + N) = O(N)
Space: O(N)

执行用时：24 ms, 在所有 Python 提交中击败了23.33%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了6.67%的用户
'''


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = map(int, str(n))
        N = len(digits)
        pos = -1  # position
        for i in range(N - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pos = i
                break
        
        if -1 == pos:
            return -1
        else:
            greaterIdx = self.findGreaterIdx(digits, N, pos)
            digits[pos], digits[greaterIdx] = digits[greaterIdx], digits[pos]
            rearrange = digits[: i + 1] + digits[i + 1: ][:: -1]
            rearrange = int(''.join(map(str, rearrange)))
            if rearrange > (1 << 31) - 1 or rearrange < 1:
                return -1
            else:
                return rearrange

    def findGreaterIdx(self, digits, N, pos):
        for i in range(N - 1, pos, -1):
            if digits[i] > digits[pos]:
                return i
    