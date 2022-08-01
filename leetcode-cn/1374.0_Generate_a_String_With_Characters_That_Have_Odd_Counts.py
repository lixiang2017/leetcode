'''
执行用时：52 ms, 在所有 Python3 提交中击败了10.53% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了30.99% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1:
            return 'a' * n 
        else:
            return 'a' + 'b' * (n - 1)
            