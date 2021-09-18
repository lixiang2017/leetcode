'''
执行用时：28 ms, 在所有 Python3 提交中击败了87.42% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了86.45% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return True if n % 4 else False


'''
执行用时：32 ms, 在所有 Python3 提交中击败了68.60% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了77.94% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


'''
bitwise

执行用时：24 ms, 在所有 Python3 提交中击败了96.84% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.36% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n & 3) != 0
        