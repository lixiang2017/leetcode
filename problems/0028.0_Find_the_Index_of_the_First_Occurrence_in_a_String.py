'''
brute force

Runtime: 37 ms, faster than 34.94% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 13.8 MB, less than 95.82% of Python3 online submissions for Find the Index of the First Occurrence in a String.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i: i + n] == needle:
                return i
        return -1

'''
brute force

Runtime: 36 ms, faster than 41.63% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 13.7 MB, less than 95.82% of Python3 online submissions for Find the Index of the First Occurrence in a String.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if all(haystack[i + j] == needle[j] for j in range(n)):
                return i
        return -1

'''
Runtime: 28 ms, faster than 86.54% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 13.9 MB, less than 54.52% of Python3 online submissions for Find the Index of the First Occurrence in a String.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            for j in range(n):
                if needle[j] != haystack[i + j]:
                    break
                if j == n - 1:
                    return i
        return -1


        