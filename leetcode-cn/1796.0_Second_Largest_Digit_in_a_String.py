'''
one pass
T: O(N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了92.08% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了74.75% 的用户
通过测试用例：301 / 301
'''
class Solution:
    def secondHighest(self, s: str) -> int:
        second = first = -1
        for ch in s:
            if ch.isdigit():
                if int(ch) > first:
                    second = first
                    first = int(ch)
                elif second < int(ch) < first:
                    second = int(ch)
        return second 
