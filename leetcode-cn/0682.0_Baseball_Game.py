'''
simulation
T: O(N)
S: O(N)

执行用时：28 ms, 在所有 Python3 提交中击败了98.84% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了96.19% 的用户
通过测试用例：39 / 39
'''
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if 'C' == op:
                stack.pop()
            elif 'D' == op:
                stack.append(stack[-1] * 2)
            elif '+' == op:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)
