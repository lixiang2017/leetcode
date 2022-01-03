'''
执行用时：32 ms, 在所有 Python3 提交中击败了68.40% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了46.01% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime('%A')




'''
蔡勒公式1

'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1
        c, y = divmod(year, 100)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        w1 = (y + y // 4 + c // 4 - 2 * c + 26 * (month + 1) // 10 + day - 1) % 7
        # w2 = (y + y // 4 + c // 4 - 2 * c + 2 * month + 3 * (month + 1) // 5  + day + 1) % 7
        return days[w1]


'''
蔡勒公式2

执行用时：24 ms, 在所有 Python3 提交中击败了98.77% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了27.00% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1
        c, y = divmod(year, 100)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # w1 = (y + y // 4 + c // 4 - 2 * c + 26 * (month + 1) // 10 + day - 1) % 7
        w2 = (y + y // 4 + c // 4 - 2 * c + 2 * month + 3 * (month + 1) // 5  + day + 1) % 7
        return days[w2]

