'''
one pass

执行用时：116 ms, 在所有 Python3 提交中击败了66.10% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了28.81% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        prev = ''
        c = 0
        for ch in s:
            if prev == ch:
                c += 1
                ans += c 
            else:
                c = 1
                ans += c 
                prev = ch 
            ans %= MOD 
        return ans 
