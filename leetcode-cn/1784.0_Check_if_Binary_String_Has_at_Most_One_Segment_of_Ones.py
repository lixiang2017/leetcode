'''
执行用时：48 ms, 在所有 Python3 提交中击败了7.43% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.86% 的用户
通过测试用例：191 / 191
'''
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not re.search('100*1', s)

'''
执行用时：40 ms, 在所有 Python3 提交中击败了40.00% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了96.57% 的用户
通过测试用例：191 / 191
'''
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not '01' in s 


'''
执行用时：40 ms, 在所有 Python3 提交中击败了40.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了49.71% 的用户
通过测试用例：191 / 191
'''
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i, n = 0, len(s)
        while i < n and s[i] == '1':
            i += 1
        while i  < n and s[i] == '0':
            i += 1
        return i == n
