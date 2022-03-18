'''
greedy + monotonic stack, T: O(N), S: O(N)

执行用时：72 ms, 在所有 Python3 提交中击败了22.04% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了25.81% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while stack and k and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        while stack and k:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or '0'


'''
执行用时：68 ms, 在所有 Python3 提交中击败了25.28% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了15.22% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while stack and k and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        if k:
            stack = stack[ :-k]
        return ''.join(stack).lstrip('0') or '0'
