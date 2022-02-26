'''
更相减损术

执行用时：88 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：161 / 161
'''
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 and num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
            
        return cnt

'''
辗转相除法

执行用时：28 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：161 / 161
'''
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 and num2:
            if num1 >= num2:
                q, r = divmod(num1, num2)
                ans += q
                num1 = r 
            else:
                num1, num2 = num2, num1 
        return ans

