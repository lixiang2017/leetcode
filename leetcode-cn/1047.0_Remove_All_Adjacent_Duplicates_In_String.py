'''
approach: Stack
Time: O(N)
Space: O(N)

执行用时：56 ms, 在所有 Python 提交中击败了80.66%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了51.04%的用户
'''

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for letter in S:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        return ''.join(stack)
