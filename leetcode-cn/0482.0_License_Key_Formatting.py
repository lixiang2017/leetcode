'''
go forwards

执行用时：68 ms, 在所有 Python3 提交中击败了37.31% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了77.89% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        us = []  # upper s
        for ch in s:
            if '-' == ch:
                continue
            if ord('a') <= ord(ch) <= ord('z'):
                ch = chr(ord(ch) - ord('a') + ord('A'))
            us.append(ch)
        N = len(us)
        # group, remainder
        g, r = divmod(N, k)
        x = 0
        ans = ''
        if r:
            ans += ''.join(us[:r])
        while x < g:
            ans += '-' + ''.join(us[r + x * k: r + (x + 1) * k])
            x += 1
        return ans[(r==0): ]


'''
执行用时：128 ms, 在所有 Python3 提交中击败了18.46% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了85.77% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = s.upper().replace('-', '')[:: -1]
        n = len(S)
        ans = ''
        for i in range(n):
            if i % k == 0 and i != 0:
                ans = '-' + ans
            ans = S[i] + ans
        return ans
        