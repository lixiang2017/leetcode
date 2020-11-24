'''
You are here!
Your runtime beats 61.69 % of python submissions.
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if 0 == size: return 0
        stack = []
        currentNumber = 0
        operation = '+'
        for i in range(size):
            currentChar = s[i]
            if currentChar.isdigit():
                currentNumber = currentNumber * 10 + int(currentChar)
            if s[i] in '+-*/' or i == len(s) - 1:
                if '-' == operation:
                    stack.append(-currentNumber)
                elif '+' == operation:
                    stack.append(currentNumber)
                elif '*' == operation:
                    stackTop = stack.pop()
                    stack.append(stackTop * currentNumber)
                elif '/' == operation:
                    stackTop = stack.pop()
                    res = abs(stackTop) / currentNumber
                    stack.append(res if stackTop > 0 else -res)
                
                # print 'stack: ', stack
                operation = currentChar
                currentNumber = 0
         
        return sum(stack)
        



'''
You are here!
Your runtime beats 99.78 % of python submissions.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s)
        