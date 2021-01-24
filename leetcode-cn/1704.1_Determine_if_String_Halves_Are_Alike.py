'''
执行结果：通过
显示详情
执行用时：
60 ms, 在所有 Python 提交中击败了6.25%的用户
内存消耗：
12.8 MB, 在所有 Python 提交中击败了93.75%的用户
'''

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(char in set('aeiouAEIOU') for char in s[:len(s) / 2]) == \
            sum(char in set('aeiouAEIOU') for char in s[len(s) / 2 : ])
