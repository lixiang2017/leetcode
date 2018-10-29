'''
Author: lixiang
Beats: 60.01%
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        i = 0
        while i < haystack_len - needle_len + 1:
            if haystack[i:i+needle_len] == needle:
                return i
            i += 1
        return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))

    haystack = "aaaaa"
    needle = "bba"
    print(Solution().strStr(haystack, needle))

    haystack = "a"
    needle = "a"
    print(Solution().strStr(haystack, needle))   # 0