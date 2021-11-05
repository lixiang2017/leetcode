'''
Binary Search
T: O(logN)
S: O(1)

Runtime: 36 ms, faster than 82.51% of Python3 online submissions for Arranging Coins.
Memory Usage: 14.2 MB, less than 70.56% of Python3 online submissions for Arranging Coins.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if m * (m + 1) // 2 <= n:
                l = m + 1
            else:
                r = m - 1
        return l - 1


'''
Runtime: 24 ms, faster than 99.40% of Python3 online submissions for Arranging Coins.
Memory Usage: 14.1 MB, less than 90.52% of Python3 online submissions for Arranging Coins.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(((2 * n + 0.25) ** 0.5 - 0.5))


'''
Runtime: 32 ms, faster than 92.00% of Python3 online submissions for Arranging Coins.
Memory Usage: 14.3 MB, less than 39.42% of Python3 online submissions for Arranging Coins.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25) ** 0.5 - 0.5)
