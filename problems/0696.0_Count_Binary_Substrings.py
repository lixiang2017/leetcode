'''
Runtime: 188 ms, faster than 63.63% of Python3 online submissions for Count Binary Substrings.
Memory Usage: 14.6 MB, less than 69.24% of Python3 online submissions for Count Binary Substrings.
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        pre = post = 0
        for i, ch in enumerate(s):
            if i == 0 or (i > 0 and ch == s[i - 1]):
                post += 1
            else:
                ans += min(pre, post)
                pre, post = post, 1
        # last pair
        ans += min(pre, post)
        return ans
        