'''
执行用时：40 ms, 在所有 Python3 提交中击败了48.84% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了99.32% 的用户
通过测试用例：294 / 294
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bits = deque()
        m, n, carry = len(a), len(b), 0
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += ord(a[i]) - ord('0')
            if j >= 0:
                s += ord(b[j]) - ord('0')
            carry, s = divmod(s, 2)
            bits.appendleft(chr(ord('0') + s))
            i -= 1
            j -= 1

        return ''.join(bits)
