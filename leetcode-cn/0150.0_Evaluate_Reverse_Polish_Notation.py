'''
approach: Stack
Time: O(N)
Space: O(N)

执行用时：32 ms, 在所有 Python 提交中击败了60.21%的用户
内存消耗：14.3 MB, 在所有 Python 提交中击败了76.44%的用户
'''


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            stack.append(token)
            while len(stack) >= 3 and stack[-1] in ['+', '-', '*', '/']:
                operator = stack.pop()
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                result = 0
                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    # Note that division between two integers should truncate toward zero.
                    result = int(operand1 * 1.0/ operand2)
                stack.append(result)

        return int(stack[-1])
