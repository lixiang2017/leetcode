'''
执行用时：40 ms, 在所有 Python3 提交中击败了87.31% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.04% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        say = ['1']
        for _ in range(n - 1):         
            next_s = ''.join(str(len(list(g))) + k for k, g in groupby(say[-1]))
            say.append(next_s)
        return say[n - 1]

'''
执行用时：40 ms, 在所有 Python3 提交中击败了87.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了65.86% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for _ in range(n - 1):         
            ans = ''.join(str(len(list(g))) + k for k, g in groupby(ans))
        return ans
        