'''
greedy

执行用时：128 ms, 在所有 Python3 提交中击败了52.56% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了89.74% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # [0, x]   y ->  [y, x + y], need x + 1 >= y
        reachable = 0
        coins.sort()
        for y in coins:
            if reachable + 1 < y:
                break
            else:
                reachable += y
        return reachable + 1
