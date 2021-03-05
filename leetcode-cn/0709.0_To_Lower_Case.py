'''

执行用时：20 ms, 在所有 Python 提交中击败了37.76%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了97.45%的用户
'''


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()



'''
执行用时：24 ms, 在所有 Python 提交中击败了12.76%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了89.29%的用户
'''

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower = ''
        for letter in str:
            if ord('A') <= ord(letter) <= ord('Z'):
                lower += chr(ord(letter) - ord('A') + ord('a'))
            else:
                lower += letter
        return lower

'''
执行用时：12 ms, 在所有 Python 提交中击败了88.27%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了54.59%的用户
'''

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(letter) - ord('A') + ord('a')) \
            if (ord('A') <= ord(letter) <= ord('Z')) else letter for letter in str])
