'''
simulation

执行用时：40 ms, 在所有 Python3 提交中击败了56.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.03% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def fractionAddition(self, expression: str) -> str:
        ans = '0/1'
        def add_sub(operand):
            if '0/1' == ans:
                return operand
            sign1 = '+' if ans[0] not in '+-' else ans[0]
            sign2 = operand[0]
            if '/' in ans:
                a, b = map(int, ans.strip('+-').split('/'))
            else:
                a, b = int(ans.strip('+-')), 1
            if '/' in operand:
                c, d = map(int, operand.strip('+-').split('/'))
            else:
                a, b = int(operand.strip('+-')), 1    

            denominator = b * d   
            numerator = (a * d if sign1 != '-' else -a * d) + (b * c if sign2 != '-' else -b * c)
            if numerator == 0:
                return '0/1'
            g = gcd(abs(numerator), denominator)
            numerator //= g 
            denominator //= g 
            return str(numerator) + '/' + str(denominator)

        prev_idx = 0
        for i, ch in enumerate(expression):
            if 0 == i:
                continue
            if ch in '+-':
                operand = expression[prev_idx: i]
                ans = add_sub(operand)
                # memo for next
                prev_idx = i 
        # last one 
        ans = add_sub(expression[prev_idx: ])
        return ans.strip('+')
