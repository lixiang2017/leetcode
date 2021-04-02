'''
Time: O(N)
Space: O(1)

执行用时：20 ms, 在所有 Python 提交中击败了73.91%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了73.91%的用户
clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
'''

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        # addition
        for i in range(N - 3, 0, -4):
            ans += i

        # first part
        first = 1
        first *= N
        if N >= 2:
            first *= (N - 1)
        if N >= 3:
            first /= (N - 2)
        ans += first

        # subtraction
        for i in range(N - 4, 0, -4):
            # sub = 1
            sub = i
            if i >= 2:
                sub *= (i - 1)
            if i >= 3:
                sub /= (i - 2)
            ans -= sub

        return ans
