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

'''
执行用时：28 ms, 在所有 Python3 提交中击败了85.80% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.78% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

'''
执行用时：24 ms, 在所有 Python3 提交中击败了95.97% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了81.19% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        def to_low(ch):
            if ord('A') <= ord(ch) <= ord('Z'):
                return chr(ord(ch) - ord('A') + ord('a'))
            return ch 
        return ''.join(map(to_low, s))



'''
执行用时：32 ms, 在所有 Python3 提交中击败了63.15% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了48.94% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        to_low = lambda ch: [ch, chr(ord(ch) - ord('A') + ord('a'))][ord('A') <= ord(ch) <= ord('Z')]
        return ''.join(map(to_low, s))


'''
执行用时：32 ms, 在所有 Python3 提交中击败了63.15% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了70.06% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(ch) | 32) if ord("A") <= ord(ch) <= ord('Z') else ch for ch in s)

              