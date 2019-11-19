#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7
#
'''
Accepted
241/241 cases passed (16 ms)
Your runtime beats 73.58 % of python submissions
Your memory usage beats 100 % of python submissions (11.7 MB)
'''
# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if 0 == num:
            return '0'

        result = []
        is_negative = False
        if num < 0:
            is_negative = True
            num = -num
        
        while num:
            result.append(str(num % 7))
            num = num / 7
        
        if is_negative:
            result.append('-')
        result = ''.join(result[::-1])

        return result
        
# @lc code=end

if __name__ == '__main__':
    num = 101
    assert Solution().convertToBase7(num) == "203"

    num = 100
    assert Solution().convertToBase7(num) == "202"


    num = -7
    assert Solution().convertToBase7(num) == "-10"

    num = 0
    assert Solution().convertToBase7(num) == '0'

    num = -1
    assert Solution().convertToBase7(num) == '-1'

    num = 7
    assert Solution().convertToBase7(num) == '10'
