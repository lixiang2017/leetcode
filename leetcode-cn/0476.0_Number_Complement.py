'''
bit manipulation
 从低位到高位模拟
T: O(31)
S: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了64.47% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了62.87% 的用户
通过测试用例：149 / 149
'''
class Solution:
    def findComplement(self, num: int) -> int:
        com = 0
        shift = 0
        while num:
            if not num & (1 << shift):  # 0
                com |= (1 << shift)
            else:  # clear low bit 1
                num &= (1 << 31) - 1 - (1 << shift)
            shift += 1
        return com


'''
bit manipulation
看num有多少位，然后构造长度相等均为1的数。异或即可。
T: O(31)
S: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了64.47% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了92.02% 的用户
通过测试用例：149 / 149
'''
class Solution:
    def findComplement(self, num: int) -> int:
        bak, ones = num, 0
        while bak:
            bak >>= 1
            ones = (ones << 1) + 1
        return num ^ ones


'''
bit manipulation
看num有多少位，然后构造长度相等均为1的数。异或即可。
T: O(31)
S: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了85.03% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了34.93% 的用户
通过测试用例：149 / 149

'''
class Solution:
    def findComplement(self, num: int) -> int:
        bak, c = num, 1
        while bak:
            bak >>= 1
            c <<= 1
        return num ^ (c - 1)
