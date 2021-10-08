'''
while * 3
T: O(N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了33.57% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了51.62% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def countSegments(self, s: str) -> int:
        seg = i = 0
        N = len(s)
        while i < N:
            # skip space
            while i < N and s[i] == ' ':
                i += 1
            non_space = 0
            while i < N and s[i] != ' ':
                non_space += 1
                i += 1
            if non_space:
                seg += 1
        return seg
