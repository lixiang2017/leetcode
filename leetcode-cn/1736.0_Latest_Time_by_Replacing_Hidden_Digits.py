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


'''
执行用时：28 ms, 在所有 Python3 提交中击败了97.49% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了64.82% 的用户
'''
class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        if t[0] == '?':
            if t[1] == '?':
                t[0], t[1] = '2', '3'
            elif t[1] <= '3':
                t[0] = '2'
            else:
                t[0] = '1'
        else:
            if t[1] == '?':
                if t[0] == '2':
                    t[1] = '3'
                else:
                    t[1] = '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return ''.join(t)


        