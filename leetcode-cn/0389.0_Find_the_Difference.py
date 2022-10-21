'''
Runtime: 36 ms, faster than 76.52% of Python3 online submissions for Find the Difference.
Memory Usage: 13.9 MB, less than 96.95% of Python3 online submissions for Find the Difference.
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tc = Counter(t)
        for ch in s:
            tc[ch] -= 1
            if tc[ch] == 0:
                tc.pop(ch)
        return list(tc.keys())[0]



'''
Runtime: 36 ms, faster than 76.52% of Python3 online submissions for Find the Difference.
Memory Usage: 14 MB, less than 79.84% of Python3 online submissions for Find the Difference.
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = sum(ord(ch) for ch in s)
        tt = sum(ord(ch) for ch in t)
        return chr(tt - ss)


'''
执行用时：36 ms, 在所有 Python3 提交中击败了87.19% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.45% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]

