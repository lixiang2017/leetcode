'''
Two Pointers

执行用时：36 ms, 在所有 Python3 提交中击败了72.88% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了18.02% 的用户
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = list(s)
        N = len(s)
        i = 0
        while i < N:
            # more than 2k, or >= k
            if i + k <= N: # i + 2 * k <= N:
                l, r = i, i + k - 1
            # fewer than k
            else:
                l, r = i, N - 1
            # reverse
            while l < r:
                ss[l], ss[r] = ss[r], ss[l]
                l, r = l + 1, r - 1

            i += 2 * k

        return ''.join(ss)


'''
执行用时：28 ms, 在所有 Python3 提交中击败了96.19% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了70.54% 的用户
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = list(s)
        for i in range(0, len(ss), 2 * k):
            ss[i: i + k] = reversed(ss[i: i + k])
        return ''.join(ss)
        