'''

执行用时：36 ms, 在所有 Python3 提交中击败了76.77% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.55% 的用户
通过测试用例：98 / 98
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = set()
        for d in range(2, int(sqrt(num)) + 1):
            if num % d == 0:
                divisors.add(d)
                divisors.add(num // d)
        return 1 != num and sum(divisors) + 1 == num 
