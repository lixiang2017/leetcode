'''
执行用时：32 ms, 在所有 Python3 提交中击败了92.32% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了21.99% 的用户
通过测试用例：123 / 123
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        while n:
            n, d = divmod(n, 10)
            product *= d 
            sum += d 
        return product - sum 
        