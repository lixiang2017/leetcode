'''
stack

单步调试，一步步完善，才通过的。

You are here!
Your runtime beats 9.36 % of python3 submissions.
You are here!
Your memory usage beats 35.56 % of python3 submissions.
'''
class Solution:
    def calculate(self, s: str) -> int:
        # SyntaxError: too many nested parentheses
        # return eval(s)
        stack = []
        num = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch in ['+', '-']:
                stack.append(num)
                stack.append(ch)
                num = 0
            elif ' ' == ch:
                continue
            elif ')' == ch:
                #
                stack.append(num)
                num = 0
                part = []
                while stack and (top := stack.pop()) != '(':
                    part.append(top)
                # process ``part`` from the end
                res = 0
                L = len(part)
                i = L - 1
                while i >= 0:
                    if L - 1 == i:
                        res += part[i]
                        i -= 1
                        continue
                    else:
                        if '+' == part[i]:
                            res += part[i - 1]
                            i -= 2
                        elif '-' == part[i]:
                            res -= part[i - 1]
                            i -= 2
                        else:
                            # print('wrong', part[i])
                            res += part[i]
                            i -= 1
                        
                stack.append(res)                
            else:
                num *= 10
                num += ord(ch) - ord('0')

        # the last num
        stack.append(num)
                
        ans = 0
        L = len(stack)
        i = 0
        while i < L:
            if '+' == stack[i]:
                ans += stack[i + 1]
                i += 2
            elif '-' == stack[i]:
                ans -= stack[i + 1]
                i += 2
            else:
                ans += stack[i]
                i += 1 
        return ans

