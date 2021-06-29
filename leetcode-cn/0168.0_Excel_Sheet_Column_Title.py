'''
执行用时：48 ms, 在所有 Python3 提交中击败了10.11% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了6.66% 的用户
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title.append(remainder)
        
        return ''.join([string.ascii_uppercase[t] for t in title[:: -1]])

        