'''
T: O(logN)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了50.42% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.51% 的用户
通过测试用例：128 / 128
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # count bits
        bits = 0
        x = n
        while x:
            x >>= 1
            bits += 1
        return (1 << bits) - n - 1


'''
举个例子 6是110 那么他的反码是他与111异或得到的001。所以找到比N大的每位都为1的数，与N进行异或。

执行用时：32 ms, 在所有 Python3 提交中击败了80.67% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了84.87% 的用户
通过测试用例：128 / 128
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ones = 1
        while ones < n:
            ones = (ones << 1) + 1
        return ones ^ n
