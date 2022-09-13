'''
执行用时：36 ms, 在所有 Python3 提交中击败了68.71% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了49.11% 的用户
通过测试用例：111 / 111
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        s_digits = sorted(digits, reverse=True)
        if digits == s_digits:
            return num 

        def max_index_after(i):
            m = i 
            for j in range(i + 1, len(digits)):
                if digits[j] >= digits[m]:
                    m = j
            return m 

        n = len(digits)
        for i in range(n - 1):
            j = max_index_after(i)
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]
                break
        return int(''.join(digits))
        