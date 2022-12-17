'''
stack
T: O(N)
S: O(N)

Runtime: 72 ms, faster than 88.75% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.3 MB, less than 96.51% of Python3 online submissions for Evaluate Reverse Polish Notation.
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                y = stack.pop()
                x = stack.pop()
                z = x + y if t == '+' else \
                    x - y if t == '-' else \
                    x * y if t == '*' else \
                    (x // y if x * y >= 0 else abs(x) // abs(y) * -1) if t == '/' else 0
                stack.append(z)
            else:
                stack.append(int(t))

        return stack.pop()

'''
["6","8","/"]
["-6","8","/"]
["6","-8","/"]
["-6","-8","/"]

0
0
0
0
'''
