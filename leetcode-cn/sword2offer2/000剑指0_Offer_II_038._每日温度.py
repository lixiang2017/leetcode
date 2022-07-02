'''
单调栈
T: O(N)
S: O(N)

执行用时：168 ms, 在所有 Python3 提交中击败了99.32% 的用户
内存消耗：22 MB, 在所有 Python3 提交中击败了38.80% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j 
            stack.append(i)
        return ans 
