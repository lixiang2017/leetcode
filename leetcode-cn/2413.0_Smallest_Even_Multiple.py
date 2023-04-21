'''
执行用时：32 ms, 在所有 Python3 提交中击败了83.88% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了15.79% 的用户
通过测试用例：150 / 150
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else 2 * n

'''
执行用时：40 ms, 在所有 Python3 提交中击败了37.99% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了19.08% 的用户
通过测试用例：150 / 150
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n & 1 == 0 else 2 * n


'''
执行用时：36 ms, 在所有 Python3 提交中击败了64.31% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了83.72% 的用户
通过测试用例：150 / 150
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return 2 * n // gcd(2, n)
        