#
# @lc app=leetcode id=1154 lang=python
#
# [1154] Day of the Year
#
'''
Accepted
246/246 cases passed (24 ms)
Your runtime beats 9.16 % of python submissions
Your memory usage beats 100 % of python submissions (11.7 MB)
'''
# @lc code=start
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day =[int(i) for i in date.split('-')]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def isLeapYear(year):
            if 0 == year % 400:
                return True
            if 0 == year % 4 and 0 != year % 100:
                return True

        if 1 == month:
            return day
        elif isLeapYear(year):
            days[1] += 1

        return sum(days[: month - 1]) + day

        
# @lc code=end

if __name__ == '__main__':
    date = "2019-01-09"
    assert Solution().dayOfYear(date) == 9

    date = "2019-02-10"
    assert Solution().dayOfYear(date) == 41

    date = "2003-03-01"
    assert Solution().dayOfYear(date) == 60

    date = "2004-03-01"
    assert Solution().dayOfYear(date) == 61
