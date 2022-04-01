'''
执行用时：44 ms, 在所有 Python3 提交中击败了24.35% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.61% 的用户
通过测试用例：160 / 160
'''
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans, n = 0, len(s)
        for i in range(n - 2):
            if len({s[i], s[i + 1], s[i + 2]}) == 3:
                ans += 1
        return ans 


'''
执行用时：44 ms, 在所有 Python3 提交中击败了24.35% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了92.41% 的用户
通过测试用例：160 / 160
'''
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans, n = 0, len(s)
        for i in range(n - 2):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i] != s[i + 2]:
                ans += 1
        return ans 
