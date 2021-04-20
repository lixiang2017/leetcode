'''

执行用时：48 ms, 在所有 Python3 提交中击败了39.47%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了62.89%的用户
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1

'''
"hello"
"ll"
"aaaaa"
"bba"
'''




'''
approach: Two Pointers
Time: O(MN)
Space :O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了39.47%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了21.27%的用户
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(haystack), len(needle)
        if N == M and haystack == needle:
            return 0

        # for i in range(N - M):   # wrong!
        for i in range(N - M + 1):
            if haystack[i: i + M] == needle:
                return i

        return -1


'''
输入：
""
""
输出：
-1
预期结果：
0

输入：
"abc"
"c"
输出：
-1
预期结果：
2
'''

