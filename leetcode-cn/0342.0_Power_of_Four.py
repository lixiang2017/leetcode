'''
Bit Manipulattion,T:O(1),S:O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了53.19% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了73.45% 的用户
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0xAAAAAAAA == 0



'''
Bit Manipulattion,T:O(1),S:O(1)
执行用时：36 ms, 在所有 Python3 提交中击败了89.43% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了94.85% 的用户
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0x2AAAAAAA == 0


'''
Bit Manipulattion,T:O(1),S:O(1)
执行用时：44 ms, 在所有 Python3 提交中击败了53.19% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了82.71% 的用户
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1

'''
执行用时：44 ms, 在所有 Python3 提交中击败了53.19% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了92.14% 的用户
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return 1 == n