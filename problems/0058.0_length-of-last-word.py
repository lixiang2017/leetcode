#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
'''
Accepted
59/59 cases passed (20 ms)
Your runtime beats 43.92 % of python submissions
Your memory usage beats 78.57 % of python submissions (11.8 MB)
'''

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split()) == 0:
            return 0
        else:
            return len(s.split()[-1])
        
# @lc code=end

if __name__ == '__main__':
    s = "Hello World"
    assert Solution().lengthOfLastWord(s) == 5

    s = ''
    assert Solution().lengthOfLastWord(s) == 0

    s = 'A word is defined as a character sequence consists of non-space characters only'
    assert Solution().lengthOfLastWord(s) == 4

    s = 'Length of Last Word'
    assert Solution().lengthOfLastWord(s) == 4

    s = " " # Line 10: IndexError: list index out of range
    assert Solution().lengthOfLastWord(s) == 0

    s = '    '
    assert Solution().lengthOfLastWord(s) == 0

    s = '    hello'
    assert Solution().lengthOfLastWord(s) == 5    

