'''
Greedy + Monotonic Stack
T: O(2N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了83.61% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了12.59% 的用户
通过测试用例：289 / 289
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = [False] * 26
        lastIndex = [0] * 26
        stack = []
        for i, ch in enumerate(s):
            lastIndex[ord(ch) - ord('a')] = i
        
        for i, ch in enumerate(s):
            if seen[ord(ch) - ord('a')]:
                continue
            
            while stack and stack[-1] > ch and lastIndex[ord(stack[-1]) - ord('a')] > i:
                seen[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(ch)
            seen[ord(ch) - ord('a')] = True

        return ''.join(stack)
