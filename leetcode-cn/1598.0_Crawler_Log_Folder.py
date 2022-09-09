'''
simulation for stack
T: O(N)
S: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了97.94% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了81.96% 的用户
通过测试用例：99 / 99
'''
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            if op == '../':
                if depth > 0:
                    depth -= 1
            elif op == './':
                continue
            else:
                depth += 1
        return depth


'''
执行用时：40 ms, 在所有 Python3 提交中击败了42.27% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了78.87% 的用户
通过测试用例：99 / 99
'''
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            if op == '../':
                if depth > 0:
                    depth -= 1
            elif op != './':
                depth += 1
        return depth
        



'''
stack
T: O(N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了69.07% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了98.97% 的用户
通过测试用例：99 / 99
'''
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for op in logs:
            if op == '../':
                if stack:
                    stack.pop()
            elif op == './':
                continue
            else:
                stack.append(op)

        return len(stack)




'''
stack

执行用时：32 ms, 在所有 Python3 提交中击败了91.30% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了38.70% 的用户
通过测试用例：99 / 99
'''
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == './':
                continue 
            elif log == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(log)
        return len(stack)
