'''
执行用时：44 ms, 在所有 Python3 提交中击败了40.53% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了24.85% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0 
        return n if n & 1 else n // 2

'''
执行用时：44 ms, 在所有 Python3 提交中击败了40.53% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了13.90% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n if n & 1 and n != 1 else n // 2
        