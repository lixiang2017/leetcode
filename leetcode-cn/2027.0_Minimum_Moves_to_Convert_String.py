'''
执行用时：36 ms, 在所有 Python3 提交中击败了75.72% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了43.93% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        ss = list(s)
        i = move = 0
        while i < n:
            if ss[i] == 'X':
                move += 1
                i += 3
            else:
                i += 1
        return move 
