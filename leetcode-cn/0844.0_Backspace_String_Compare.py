'''
stack simulation
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


'''
stack simulation
T: O(M + N)
S: O(M + N)

执行用时：36 ms, 在所有 Python3 提交中击败了63.49% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.91% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(u):
            uu = []
            for ch in u:
                if ch != '#':
                    uu.append(ch)
                elif uu:
                    uu.pop()
            return ''.join(uu)

        return build(s) == build(t)


'''
two pointers, 倒序 skip
T: O(M + N), S: O(1)

感想：
代码写得多了，自然而然就想着复用。比如，这里把 s 和 t 同用一个函数处理。
同时，主函数中 while 中采用 or 避免了退出 while 之后的再次讨论。

执行用时：40 ms, 在所有 Python3 提交中击败了35.63% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了76.25% 的用户
通过测试用例：114 / 114
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        i, j = ns - 1, nt - 1

        def findValidLetter(st, ij):
            skip = 0
            while ij >= 0:
                if st[ij] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    return st[ij], ij - 1
                ij -= 1
            return None, -1

        while i >= 0 or j >= 0:
            # find each valid letter in s and t from the end to beginning
            valid_ss, i = findValidLetter(s, i) 
            valid_tt, j = findValidLetter(t, j)
            if valid_ss != valid_tt:
                return False

        return True


