'''
执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了60.00%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了55.79%的用户

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了24.21%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了57.89%的用户
'''


class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = list(time)
        if '?' == time[0]:
            if '?' == time[1]: # ??:..
                time[0] = '2'
                time[1] = '3'
            else: # ?x:..
                # if ord(time[1]) > ord('3'):  # ok
                if int(time[1]) > 3:
                    time[0] = '1'
                else:
                    time[0] = '2'
        else:
            if '?' == time[1]: # x?:..
                if '1' == time[0] or '0' == time[0]:
                    time[1] = '9'
                else:
                    time[1] = '3'

        if '?' == time[3]: time[3] = '5'
        if '?' == time[4]: time[4] = '9'
        return ''.join(time)
