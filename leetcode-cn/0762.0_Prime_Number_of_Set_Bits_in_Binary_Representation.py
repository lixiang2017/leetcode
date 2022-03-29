'''
执行用时：164 ms, 在所有 Python3 提交中击败了76.64% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了14.23% 的用户
通过测试用例：202 / 202
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = set([2, 3, 5, 7, 11, 13, 17, 19])
        return len([x for x in range(left, right + 1) if bin(x).count('1') in cnt])
        