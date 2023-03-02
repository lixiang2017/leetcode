'''
执行用时：32 ms, 在所有 Python3 提交中击败了87.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.21% 的用户
通过测试用例：33 / 33
'''
class Solution:
    def printBin(self, num: float) -> str:
        ans = ['0', '.']
        while num > 0 and len(ans) < 32:
            num *= 2
            if num >= 1:
                ans.append('1')
                num -= 1
            else:
                ans.append('0')

        if num > 0:
            return 'ERROR'
        else:
            return ''.join(ans)
