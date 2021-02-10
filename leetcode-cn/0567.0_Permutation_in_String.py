'''
approach: Sort
Time: O(MlogM + MlogM * (N-M) ), where M is the length of s1 and N is the length of s2.
Space: O(1)

执行结果：通过
显示详情
执行用时：5224 ms, 在所有 Python 提交中击败了13.27%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了5.10%的用户
'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1, s2 = list(s1), list(s2)
        size1, size2 = len(s1), len(s2)
        s1.sort()
        for i in range(size2 - size1 + 1):
            part = s2[i: i + size1]
            part.sort()
            if part == s1:
                return True
        return False
