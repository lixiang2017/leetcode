'''
合并同类项，系数化为1
simulation + string parse

"-x=-1"

执行用时：44 ms, 在所有 Python3 提交中击败了16.15% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了27.95% 的用户
通过测试用例：59 / 59
'''
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')

        def parse(part):
            x = zero = 0
            p = ''
            positive = True
            for ch in part:
                if ch in '+-':
                    if p and p[-1] == 'x':
                        x += int(p[: -1] or 1) * (-1 if not positive else 1)
                    else:
                        zero += int(p or 0) * (-1 if not positive else 1)
                    # reset to ''
                    positive = (ch == '+')
                    p = ''
                else:
                    p += ch 
            # last p 
            if p[-1] == 'x':
                x += int(p[: -1] or 1) * (-1 if not positive else 1)
            else:
                zero += int(p or 0) * (-1 if not positive else 1)
            return x, zero

        # coefficient, zero
        left_x, left_0 = parse(left)
        right_x, right_0 = parse(right)
        x = left_x - right_x
        zero = right_0 - left_0
        if x == 0:
            if zero == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return f'x={zero // x}' 

