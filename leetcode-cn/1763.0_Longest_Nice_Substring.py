'''
执行用时：136 ms, 在所有 Python3 提交中击败了24.04% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了75.96% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ''
        for i in range(n - 1):
            for j in range(n, i, -1):
                # j - i !!!, not j - i + 1
                if j - i <= len(ans):
                    continue
                seen = set(s[i: j])
                nice = True
                for chl, chu in zip(string.ascii_lowercase, string.ascii_uppercase):
                    if (chl in seen and chu not in seen) or (chl not in seen and chu in seen):
                        nice = False
                        break
                if nice:                
                    ans = s[i: j]
                    print(ans)

        return ans 

