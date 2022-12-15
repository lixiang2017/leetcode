'''
simulation

执行用时：48 ms, 在所有 Python3 提交中击败了25.37% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了99.02% 的用户
通过测试用例：216 / 216
'''
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = 0
        for ch in s:
            x = ord(ch) - ord('a') + 1
            while x:
                t += (x % 10)
                x //= 10
        for _ in range(k - 1):
            next_t = 0
            while t:
                next_t += (t % 10)
                t //= 10
            t = next_t
        return t
