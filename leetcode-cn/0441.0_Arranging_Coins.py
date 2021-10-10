'''
binary search
T: O(logN)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了67.24% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了72.58% 的用户
通过测试用例：1335 / 1335
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if (mid + 1) * mid // 2 <= n:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1


'''
T: O(N)
S: O(1)

执行用时：632 ms, 在所有 Python3 提交中击败了38.11% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了98.98% 的用户
通过测试用例：1335 / 1335
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 0
        while n > r:
            r += 1
            n -= r
        return r


'''
执行用时：36 ms, 在所有 Python3 提交中击败了78.50% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了13.31% 的用户
通过测试用例：1335 / 1335
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)
