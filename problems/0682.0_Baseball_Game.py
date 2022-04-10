'''
Runtime: 60 ms, faster than 46.41% of Python3 online submissions for Baseball Game.
Memory Usage: 14.1 MB, less than 74.69% of Python3 online submissions for Baseball Game.
'''
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)
