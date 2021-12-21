'''
执行用时：68 ms, 在所有 Python3 提交中击败了57.18% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.00% 的用户
通过测试用例：10957 / 10957
'''
class Solution:
    def isLeapYear(self, year: int) -> bool:
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

    def dayOfYear(self, date: str) -> int:
        #             1   2   3   4   5   6
        month2days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
        year, month, day = list(map(int, date.split('-')))
        return sum(month2days[: month - 1]) + day + [0, 1][self.isLeapYear(year) and month > 2]

'''
执行用时：48 ms, 在所有 Python3 提交中击败了98.87% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.15% 的用户
通过测试用例：10957 / 10957
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        #       1   2   3   4   5   6
        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        if year != 1900 and year % 4 == 0:
            days[1] += 1
        return sum(days[: month - 1]) + day

'''
执行用时：104 ms, 在所有 Python3 提交中击败了14.65% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了19.72% 的用户
通过测试用例：10957 / 10957
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        import time
        return time.strptime(date, "%Y-%m-%d")[-2]

'''
"2019-02-10"
time.struct_time(tm_year=2019, tm_mon=2, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=41, tm_isdst=-1)
'''

'''
执行用时：108 ms, 在所有 Python3 提交中击败了14.37% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了67.04% 的用户
通过测试用例：10957 / 10957
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        import time
        return time.strptime(date, "%Y-%m-%d").tm_yday


