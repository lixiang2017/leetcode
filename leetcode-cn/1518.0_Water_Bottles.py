'''
执行用时：36 ms, 在所有 Python3 提交中击败了28.57% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.11% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
        