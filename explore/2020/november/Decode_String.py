'''
You are here!
Your runtime beats 39.80 % of python submissions.
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                # append
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                # pop
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * num
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curString += c
        
        return curString




'''
You are here!
Your runtime beats 39.80 % of python submissions.
'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s




