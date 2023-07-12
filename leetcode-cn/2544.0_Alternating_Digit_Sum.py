'''
执行用时：40 ms, 在所有 Python3 提交中击败了63.76% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了13.30% 的用户
通过测试用例：118 / 118
'''
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0
        for i, ch in enumerate(s):
            if i & 1:
                ans -= int(ch)
            else:
                ans += int(ch)
        return ans 
    

'''
执行用时：52 ms, 在所有 Python3 提交中击败了7.34% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了52.30% 的用户
通过测试用例：118 / 118
'''
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = digits_cnt = 0
        while n:
            digits_cnt += 1
            n, x = divmod(n, 10)
            if digits_cnt & 1:
                ans -= x
            else:
                ans += x 
        
        return ans if digits_cnt % 2 == 0 else -ans

'''
执行用时：48 ms, 在所有 Python3 提交中击败了20.64% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了48.17% 的用户
通过测试用例：118 / 118
'''
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans, sign = 0, 1
        while n:
            n, x = divmod(n, 10)
            ans -= sign * x 
            sign = -sign 
        return sign * ans 

'''
执行用时：40 ms, 在所有 Python3 提交中击败了63.76% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了64.68% 的用户
通过测试用例：118 / 118
'''
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans, sign = 0, -1
        while n:
            n, x = divmod(n, 10)
            ans -= sign * x 
            sign = -sign 
        return sign * ans 

'''
ref:
https://leetcode.cn/problems/alternating-digit-sum/solution/bu-yong-fu-hao-bian-liang-de-jian-ji-zuo-1zz5/

执行用时：52 ms, 在所有 Python3 提交中击败了7.34% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了52.30% 的用户
通过测试用例：118 / 118
'''
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        while n:
            ans = n % 10 - ans 
            n //= 10
        return ans 


