'''
执行用时：164 ms, 在所有 Python3 提交中击败了48.65% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了40.99% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        cnt = len(b) // len(a)
        s0 = a * cnt 
        s1 = a * (cnt + 1)
        s2 = a * (cnt + 2)
        if b in s0:
            return cnt 
        elif b in s1:
            return cnt + 1
        elif b in s2:
            return cnt + 2
        else:
            return -1
            