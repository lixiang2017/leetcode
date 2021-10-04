'''
执行用时：28 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def minimumMoves(self, s: str) -> int:
        move = i = 0
        N = len(s)
        while i < N:
            if s[i] == 'X':
                move += 1
                i += 3
            else:
                i += 1

        return move
