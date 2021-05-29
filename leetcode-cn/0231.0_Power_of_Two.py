'''
T:O(32),S:O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了49.22% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了70.16% 的用户
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # edge case
        if n < 0:
            return False
        cnt = 0
        while n:
            cnt += 1
            n &= n - 1
        return 1 == cnt


'''
T:O(1),S:O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了49.22% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了48.49% 的用户
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 0 == n & (n - 1)


'''
T:O(1),S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了97.06% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了77.17% 的用户
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n


'''
T:O(1),S:O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了89.66% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了92.27% 的用户
'''
class Solution:
    BIG = 1 << 30
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and self.BIG % n == 0

'''
T:O(1),S:O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了49.22% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了78.69% 的用户
'''
class Solution:
    BIG = 2 ** 30
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Solution.BIG % n == 0

'''
T:O(1),S:O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了74.63% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了90.53% 的用户
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

'''
T:O(1),S:O(1)
执行用时：36 ms, 在所有 Python3 提交中击败了89.66% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了78.69% 的用户
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n ^ (n - 1) == 2 * n - 1



