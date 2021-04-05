'''
approach: Hash Set + DP

执行用时：652 ms, 在所有 Python 提交中击败了99.69% 的用户
内存消耗：17.1 MB, 在所有 Python 提交中击败了31.19% 的用户
ref:
https://leetcode-cn.com/problems/ones-and-zeroes/solution/pythonjian-dan-yi-dong-de-jie-fa-by-semi-9fu3/
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        choices = {(0, 0, 0)} # (0s, 1s, length of set)
        contains = [(oneStr.count('0'), oneStr.count('1')) for oneStr in strs]
        for zero, one in contains:
            choices |= {(zero + z, one + o, cnt + 1) for z, o, cnt in choices \
                if zero + z <= m and one + o <= n}
        return max(cnt for _, _, cnt in choices)
