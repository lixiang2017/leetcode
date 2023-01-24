'''
simulation

执行用时：44 ms, 在所有 Python3 提交中击败了40.52% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.17% 的用户
通过测试用例：227 / 227
'''
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = prev = 0
        for upper, percent in brackets:
            if income < prev:
                break 
            ans += (min(upper, income) - prev) * percent
            prev = upper 
        return ans * 0.01
