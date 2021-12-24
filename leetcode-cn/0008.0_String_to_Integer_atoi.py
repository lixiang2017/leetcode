'''
执行用时：40 ms, 在所有 Python3 提交中击败了41.02% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了44.06% 的用户
通过测试用例：1082 / 1082
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = (1 << 31) - 1, -(1 << 31)
        s = s.strip()
        n = len(s)
        sign = '+'
        ans = 0
        i = 0
        while i < n:
            if i == 0 and not s[0].isdigit():
                if s[0] in '+-':
                    sign = s[0]
                else:
                    return ans 
            elif s[i].isdigit():
                ans = ans * 10 + int(s[i])
            else:
                break
            # out of range
            if sign == '+' and ans >= MAX:
                return MAX 
            elif sign == '-' and -ans <= MIN:
                return MIN 
            i += 1

        return [ans, -ans][sign == '-']

'''
执行用时：32 ms, 在所有 Python3 提交中击败了86.22% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了64.51% 的用户
通过测试用例：1082 / 1082
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = (1 << 31) - 1, -(1 << 31)
        s = s.strip()
        n = len(s)
        sub = re.findall('^[+-]?\d+', s)
        if not sub or sub[0] == '' or sub[0] == '+' or sub[0] == '-':
            return 0
        else:
            x = int(sub[0])
            if x >= MAX:
                return MAX 
            elif x <= MIN:
                return MIN
            else:
                return x

