'''
T:O(7),S:O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了91.49% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了34.57% 的用户
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for t in columnTitle:
            num *= 26 
            num += ord(t) - ord('A') + 1

        return num