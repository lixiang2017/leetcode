'''
iteration

执行用时：68 ms, 在所有 Python3 提交中击败了84.46% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了39.06% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        i = 0 
        for l in range(2, n + 1):
            i = (i + m) % l 
        return i 


'''
recursion

执行用时：180 ms, 在所有 Python3 提交中击败了18.72% 的用户
内存消耗：110.4 MB, 在所有 Python3 提交中击败了11.31% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0 
        return (self.lastRemaining(n - 1, m) + m) % n   

