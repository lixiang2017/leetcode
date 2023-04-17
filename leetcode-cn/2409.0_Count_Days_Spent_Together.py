'''
执行用时：36 ms, 在所有 Python3 提交中击败了68.29% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了89.63% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def dayth(date: str) -> int:
            m, d = map(int, date.split('-'))
            return sum(days[: m - 1]) + d
        
        aa, la, ab, lb = map(dayth, [arriveAlice, leaveAlice, arriveBob, leaveBob])
        return max(0, min(la, lb) - max(aa, ab) + 1)
