#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
'''
Accepted
76/76 cases passed (20 ms)
Your runtime beats 61.16 % of python submissions
Your memory usage beats 37.82 % of python submissions (11.9 MB)
'''

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        print s
        stack = []
        if s == '':
            return True
        elif len(s) % 2 == 1:
            return False

        l = list(s)
        while l != []:
            c = l.pop()
            if c in [')', ']', '}']:
                stack.append(c)
            else:
                if stack == []:
                    return False
                top_char = stack.pop()
                if top_char == ')' and c == '(':
                    continue
                elif top_char == ']' and c == '[':
                    continue
                elif top_char == '}' and c == '{':
                    continue
                else:
                    return False

        if stack == []:
            return True
        else:
            return False
        
# @lc code=end

if __name__ == '__main__':
    s = ''
    assert Solution().isValid(s)

    s = "()"
    assert Solution().isValid(s)

    s = "()[]{}"
    assert Solution().isValid(s)

    s = "(]"
    assert not Solution().isValid(s)

    s = "([)]"
    assert not Solution().isValid(s)

    s = "{[]}"
    assert Solution().isValid(s)

    s = '(('
    assert not Solution().isValid(s)

    s = '))'
    assert not Solution().isValid(s)
