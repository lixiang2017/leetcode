'''

执行用时：20 ms, 在所有 Python3 提交中击败了99.70% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了80.06% 的用户
通过测试用例：204 / 204
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = bin(num)
        return b.count('1') + len(b) - 3


'''
执行用时：32 ms, 在所有 Python3 提交中击败了72.21% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了23.57% 的用户
通过测试用例：204 / 204
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            ans += 1
        return ans

