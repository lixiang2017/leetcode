'''
执行用时：36 ms, 在所有 Python3 提交中击败了51.08% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了64.00% 的用户
通过测试用例：1101 / 1101

'''
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            x = 0
            while num:
                x += num % 10
                num //= 10
            num = x
        return num 
