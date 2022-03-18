'''
执行用时：48 ms, 在所有 Python3 提交中击败了8.17% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了64.20% 的用户
通过测试用例：110 / 110
'''
class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", 
                 "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                 "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        
        d, m, y = date.split()
        d = d[: -2]
        if len(d) < 2:
            d = '0' + d
        m = month[m]
        return '{}-{}-{}'.format(y, m, d)

