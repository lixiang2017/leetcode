'''
simulation
T: O(M + N)
S: O(M + N)

执行用时：40 ms, 在所有 Python3 提交中击败了35.63% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了89.34% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def simulate(u):
            uu = []
            for ch in u:
                if ch == '#':
                    if uu:
                        uu.pop()
                else:
                    uu.append(ch)
            return uu

        return simulate(s) == simulate(t)
