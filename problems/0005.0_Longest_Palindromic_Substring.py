'''
中心扩散法, 需要分奇偶讨论
T： O（N^2）
S: O(1)

Runtime: 3307 ms, faster than 21.00% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.9 MB, less than 59.59% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # longest left index and right index 
        left = right = 0
        for i in range(n):
            # odd
            step = 0
            while 0 <= i - step < n and 0 <= i + step < n and s[i - step] == s[i + step]:
                if 2 * step + 1 > right - left:
                    left = i - step
                    right = i + step + 1
                step += 1
            # even 
            step = 0
            while 0 <= i - step < n and 0 <= i + step + 1 < n and s[i - step] == s[i + step + 1]:
                if 2 * step + 2 > right - left:
                    left = i - step
                    right = i + step +  2
                step += 1
        return s[left: right]