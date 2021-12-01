'''
执行用时：32 ms, 在所有 Python3 提交中击败了63.29% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.31% 的用户
通过测试用例：71 / 71
'''
'''
1 digit,  1 - 9, (9 - 1 + 1) * 1
2 digits, 10 - 99, (99 - 10 + 1) * 2
3 digits, 100 - 999, (999 - 100 + 1) * 3
4 digits, 1000 - 9999, (9999 - 1000 + 1) * 4
5 digits, 10000 - 99999, (99999 - 10000 + 1) * 5
6 digits, 100000 - 999999, (999999 - 100000 + 1) * 6
...
n digits, ...., (10 ** n - 10 ** (n-1)) * n
'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        # x digits
        x = 1
        cnt = 0
        # cnt for x digits
        cx = (10 ** x - 10 ** (x - 1)) * x
        while cnt + cx <= n:
            cnt += cx
            x += 1
            cx = (10 ** x - 10 ** (x - 1)) * x
        
        more, false_remain = divmod(n - cnt + x - 1, x)
        # xth digit for the last number
        xth = x - ((cnt + more * x) - n) - 1
        number = (10 ** (x - 1)) + more - 1
        ch = str(number)[xth]
        return int(ch)
        
