'''
执行用时：108 ms, 在所有 Python3 提交中击败了31.75% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        return max(self.maxLongest(text), self.maxLongest(list(reversed(text))))

    def maxLongest(self, text):
        c, n = Counter(text), len(text)
        if len(c) == 1:
            return n 
        ans, i = 1, 0
        while i < n:
            diff = 0
            j = i + 1
            diff_idx = j
            while j < n and diff <= 1:
                if text[j] != text[i]:
                    diff += 1
                    if diff_idx != i + 1:
                        diff_idx = j
                    if diff == 2:
                        break
                j += 1

            if j - i <= c[text[i]]:
                ans = max(ans, j - i)
            else:
                ans = max(ans, j - i - 1)
            i = diff_idx
        return ans 
