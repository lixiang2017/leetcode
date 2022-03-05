'''
simulation
T: O(2N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了76.68% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了90.62% 的用户
通过测试用例：151 / 151
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushn, popn = len(pushed), len(popped)
        if pushn != popn:
            return False
        stack = []
        i = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == popn

'''
执行用时：40 ms, 在所有 Python3 提交中击败了56.49% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了43.27% 的用户
通过测试用例：151 / 151
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushn, popn = len(pushed), len(popped)
        if pushn != popn:
            return False
        stack = []
        i = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return stack == []
        