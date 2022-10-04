'''
stack
T: O(N)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了49.57% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了61.74% 的用户
通过测试用例：115 / 115
'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif left > 0:
                left -= 1
            else:
                right += 1
        return left + right 

