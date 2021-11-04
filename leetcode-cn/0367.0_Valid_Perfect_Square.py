'''
binary search

执行用时：32 ms, 在所有 Python3 提交中击败了67.46% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了10.88% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
