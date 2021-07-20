'''
T:O(N),S:O(1)
执行用时：52 ms, 在所有 Python3 提交中击败了87.65% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了18.63% 的用户
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = -1
        N = len(num)
        for i in range(N - 1, -1, -1):
            if int(num[i]) % 2:
                odd = i
                break
        
        return num[: odd + 1] if odd != -1 else ''
