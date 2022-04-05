'''
执行用时：164 ms, 在所有 Python3 提交中击败了76.64% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了14.23% 的用户
通过测试用例：202 / 202
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = set([2, 3, 5, 7, 11, 13, 17, 19])
        return len([x for x in range(left, right + 1) if bin(x).count('1') in cnt])


'''
执行用时：148 ms, 在所有 Python3 提交中击败了91.67% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了26.39% 的用户
通过测试用例：202 / 202
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = set([2, 3, 5, 7, 11, 13, 17, 19])
        return sum(bin(x).count('1') in cnt for x in range(left, right + 1))

'''
执行用时：168 ms, 在所有 Python3 提交中击败了77.43% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了44.10% 的用户
通过测试用例：202 / 202
'''
# 665772的二进制表示是0000 0000 0000 1010 0010 1000 1010 1100，所有的1都在质数位置。
#                                 19 17  13  11   7  5 3 2
# In [75]: int('0000 0000 0000 1010 0010 1000 1010 1100'.replace(' ', ''), 2)
# Out[75]: 665772

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(665772 >> bin(x).count('1') & 1  for x in range(left, right + 1))


'''
执行用时：116 ms, 在所有 Python3 提交中击败了98.26% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了44.10% 的用户
通过测试用例：202 / 202
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return sum(665772 >> x.bit_count() & 1  for x in range(left, right + 1))


'''
执行用时：452 ms, 在所有 Python3 提交中击败了27.78% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了68.40% 的用户
通过测试用例：202 / 202
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def bitCount(x):
            c = 0
            while x:
                c += 1
                x &= x - 1
            return c 

        return sum(665772 >> bitCount(x) & 1  for x in range(left, right + 1))

