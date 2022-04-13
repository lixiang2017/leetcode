'''
排列组合

执行用时：40 ms, 在所有 Python3 提交中击败了38.54% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了52.56% 的用户
通过测试用例：9 / 9
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        c = [
            1,
            9,
            9 * 9,
            9 * 9 * 8,
            9 * 9 * 8 * 7,
            9 * 9 * 8 * 7 * 6,
            9 * 9 * 8 * 7 * 6 * 5,
            9 * 9 * 8 * 7 * 6 * 5 * 4,
            9 * 9 * 8 * 7 * 6 * 5 * 4 * 3,
        ]
        return sum(c[: n + 1])


'''
执行用时：40 ms, 在所有 Python3 提交中击败了38.54% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.76% 的用户
通过测试用例：9 / 9
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans, init = 1, 9
        i = 1 
        while i <= n:
            ans += init 
            init *= (9 - i + 1)
            i += 1
        return ans 

