'''
执行用时：32 ms, 在所有 Python3 提交中击败了71.57% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了45.49% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        m, n = divmod(numerator, denominator)
        int_part = str(m)
        if not n:
            return sign + int_part
        decimal_part = []
        dic = {}   # remainder -> index
        i = 0
        while n and n not in dic:
            dic[n] = i
            i += 1
            m, n = divmod(n* 10, denominator)
            decimal_part.append(str(m))
        if not n:
            ans = sign + int_part + '.' + ''.join(decimal_part)
        else:
            decimal_part.insert(dic[n], '(')
            decimal_part.append(')')
            ans = sign + int_part + '.' + ''.join(decimal_part)
        return ans
        
        